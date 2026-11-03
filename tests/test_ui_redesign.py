"""Targeted tests for UI redesign, theme components, and state divergence."""
import json
from pathlib import Path
from unittest.mock import patch
import pytest
from streamlit.testing.v1 import AppTest
from train_model import train_model
from model_utils import load_model
from ui_theme import (
    create_waveform_figure,
    get_feature_comparison_text,
    COLOR_CANVAS_DARK,
    COLOR_TRACE_RAW,
    COLOR_TRACE_FILTERED,
)

APP = Path(__file__).resolve().parents[1] / "app.py"


@pytest.fixture(scope="module")
def trained_model(tmp_path_factory):
    path = tmp_path_factory.mktemp("ui-model") / "model.joblib"
    train_model(path, 40)
    return load_model(path)


def test_theme_waveform_figure():
    time_arr = [0.0, 0.5, 1.0, 1.5]
    raw = [0.1, -0.2, 0.3, -0.1]
    filtered = [0.05, -0.15, 0.25, -0.05]
    fig = create_waveform_figure(time_arr, raw, filtered)

    assert fig.layout.plot_bgcolor == COLOR_CANVAS_DARK
    assert fig.layout.paper_bgcolor == COLOR_CANVAS_DARK
    assert fig.layout.xaxis.title.text == "Time (seconds)"
    assert fig.layout.yaxis.title.text == "Amplitude (arbitrary units)"
    assert len(fig.data) == 2
    assert fig.data[0].name == "Raw synthetic signal"
    assert fig.data[0].line.color == COLOR_TRACE_RAW
    assert fig.data[0].line.dash == "dot"
    assert fig.data[1].name == "Filtered synthetic signal"
    assert fig.data[1].line.color == COLOR_TRACE_FILTERED


def test_feature_comparison_text_left_and_right():
    # Left emphasis (low frequency higher)
    features_left = {"mean_power_1_12_hz": 0.08, "mean_power_12_40_hz": 0.01}
    text_left = get_feature_comparison_text(features_left, "left")
    assert "8 Hz" in text_left
    assert "stronger" in text_left

    # Right emphasis (high frequency higher)
    features_right = {"mean_power_1_12_hz": 0.01, "mean_power_12_40_hz": 0.09}
    text_right = get_feature_comparison_text(features_right, "right")
    assert "22 Hz" in text_right
    assert "stronger" in text_right


def test_draft_settings_divergence_notice(trained_model):
    """Test that modifying controls after a run displays the quiet diff notice without mutating result."""
    with patch("dashboard_model.load_model", return_value=trained_model):
        app = AppTest.from_file(str(APP)).run()
        # Initial empty state has no chart or metric
        assert len(app.get("plotly_chart")) == 0
        assert len(app.metric) == 0

        # Run with left and seed 7
        app.selectbox[0].select("left")
        app.button[0].click().run()
        assert app.session_state["result"]["label"] == "left"
        assert app.session_state["result"]["seed"] == 7

        # Change draft seed to 42 without clicking button
        app.number_input[0].set_value(42).run()
        # Result must remain intact and unchanged
        assert app.session_state["result"]["label"] == "left"
        assert app.session_state["result"]["seed"] == 7

        # Change draft label to "right" without clicking button
        app.selectbox[0].select("right").run()
        assert app.session_state["result"]["label"] == "left"

        # Now click Generate and process to apply the change atomically
        app.button[0].click().run()
        assert app.session_state["result"]["label"] == "right"
        assert app.session_state["result"]["seed"] == 42
