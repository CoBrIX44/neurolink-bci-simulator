from pathlib import Path
from unittest.mock import patch
import pytest
from streamlit.testing.v1 import AppTest
from train_model import train_model
from model_utils import load_model
import json

APP = Path(__file__).resolve().parents[1] / "app.py"


@pytest.fixture(scope="module")
def trained(tmp_path_factory):
    path = tmp_path_factory.mktemp("app-model") / "model.joblib"
    train_model(path, 40)
    return load_model(path)


def test_dashboard_both_labels_and_persistence(trained):
    with patch("dashboard_model.load_model", return_value=trained):
        app = AppTest.from_file(str(APP)).run()
        assert not app.exception
        assert "not live brain data" in app.warning[0].value
        for label in ("left", "right"):
            app.selectbox[0].select(label)
            app.button[0].click().run()
            assert not app.exception and not app.error
            assert app.metric[0].value == label
            assert len(app.get("plotly_chart")) == 1
            figure = json.loads(app.get("plotly_chart")[0].proto.spec)
            assert figure["layout"]["xaxis"]["title"]["text"] == "Time (seconds)"
            assert figure["layout"]["yaxis"]["title"]["text"] == "Amplitude (arbitrary units)"
            assert figure["data"][0]["line"]["dash"] == "dot"
            assert len(app.table) == 2
            assert app.session_state["result"]["label"] == label
        app.number_input[0].set_value(99).run()
        assert app.session_state["result"]["seed"] == 7


@pytest.mark.parametrize("failure", [OSError("Model could not be read. Check file permissions."),
                                    ValueError("Invalid input; check sampling rate.")])
def test_dashboard_error(failure):
    with patch("dashboard_model.load_model", side_effect=failure):
        app = AppTest.from_file(str(APP)).run()
        app.button[0].click().run()
        assert not app.exception
        assert app.error[0].value == str(failure)
        assert len(app.warning) == 1
        assert len(app.get("plotly_chart")) == 0


def test_failed_processing_clears_previous_result(trained):
    with patch("dashboard_model.load_model", return_value=trained):
        app = AppTest.from_file(str(APP)).run()
        app.button[0].click().run()
        assert len(app.metric) == 1
    with patch("dashboard_model.load_model", side_effect=ValueError("Retrain the model.")):
        app.button[0].click().run()
        assert not app.exception
        assert len(app.metric) == 0 and len(app.error) == 1


def test_cursor_changes_only_on_successful_processing(trained):
    with patch("dashboard_model.load_model", return_value=trained):
        app = AppTest.from_file(str(APP)).run()
        app.checkbox[0].check().run()
        app.button(key="process").click().run()
        assert app.session_state["cursor_position"] == 40
        app.number_input[0].set_value(8).run()
        assert app.session_state["cursor_position"] == 40
        app.selectbox[0].select("right").run()
        app.button(key="process").click().run()
        assert app.session_state["cursor_position"] == 50
        app.button(key="process").click().run()
        assert app.session_state["cursor_position"] == 60
        app.button(key="reset_cursor").click().run()
        assert app.session_state["cursor_position"] == 50
    with patch("dashboard_model.load_model", side_effect=ValueError("Retrain.")):
        app.button(key="process").click().run()
        assert app.session_state["cursor_position"] == 50


def test_fresh_deployment_without_model():
    from dashboard_model import synthetic_demo_model
    synthetic_demo_model.clear()
    try:
        with patch("dashboard_model.load_model", side_effect=FileNotFoundError), \
             patch("dashboard_model.train_model", wraps=train_model) as train:
            app = AppTest.from_file(str(APP)).run()
            for label in ("left", "right"):
                app.selectbox[0].select(label).run()
                app.button(key="process").click().run()
                assert not app.exception and not app.error
                assert app.metric[0].value == label
            train.assert_called_once_with(path=None)
    finally:
        synthetic_demo_model.clear()
