"""Comprehensive test suite for the approved Google Stitch NeuroLink redesign.

Validates:
- All five screens (Landing, Studio, Signal Processing, Classification Lab, Learn BCI)
- Multi-page query parameter navigation
- Signal physical telemetry metrics (Peak-to-Peak, RMS, SNR, Drift)
- Scientific disclaimer and transparency wording across screens
- Real backend integration
"""
import json
import os
from pathlib import Path
from unittest.mock import patch
import pytest
from streamlit.testing.v1 import AppTest
from train_model import train_model
from model_utils import load_model
from ui_theme import compute_signal_metrics, create_waveform_figure, get_feature_comparison_text

APP = Path(__file__).resolve().parents[1] / "app.py"


@pytest.fixture(scope="module")
def trained_model(tmp_path_factory):
    path = tmp_path_factory.mktemp("stitch-model") / "model.joblib"
    train_model(path, 40)
    return load_model(path)


def test_landing_screen_renders_successfully():
    """Verify Screen 01 (Introduction / Landing) displays key architectural content."""
    # When query param is set to landing
    app = AppTest.from_file(str(APP))
    app.query_params["page"] = "landing"
    app.run()
    assert not app.exception
    # Check that hero headline exists in rendered markdown
    md_text = " ".join(item.value for item in app.markdown)
    assert "What happens between a brain signal and a digital command?" in md_text
    assert "256 Hz" in md_text
    assert "Launch Experiment Studio" in md_text
    assert "Five-Stage BCI Simulation Pipeline" in md_text
    assert "not live brain data" in md_text


def test_signal_processing_screen_renders_and_navigates_stages():
    """Verify Screen 03 (Signal Processing) renders the 5-stage pipeline."""
    app = AppTest.from_file(str(APP))
    app.query_params["page"] = "signal-processing"
    app.run()
    assert not app.exception
    md_text = " ".join(item.value for item in app.markdown)
    assert "The Mathematical Transformation of Neural Voltages" in md_text
    assert "Five-Stage BCI Signal Architecture" in md_text
    assert "Why 1–40 Hz Zero-Phase Butterworth Filtering?" in md_text
    assert "filtfilt" in md_text

    # Click stage 2 button
    app.button[1].click().run()
    assert not app.exception
    assert app.session_state["selected_stage"] == 2


def test_classification_lab_screen_renders():
    """Verify Screen 04 (Classification Lab) displays 2D decision boundary and telemetry."""
    app = AppTest.from_file(str(APP))
    app.query_params["page"] = "classification-lab"
    app.run()
    assert not app.exception
    md_text = " ".join(item.value for item in app.markdown)
    assert "Feature Space" in md_text and "Logistic Regression Classification" in md_text
    assert "2D Spectral Power Decision Boundary" in md_text
    assert "never human thought certainty" in md_text
    assert "WEIGHT VECTOR" in md_text


def test_learn_bci_monograph_renders():
    """Verify Screen 05 (Learn BCI) displays complete educational curriculum and team table."""
    app = AppTest.from_file(str(APP))
    app.query_params["page"] = "learn-bci"
    app.run()
    assert not app.exception
    md_text = " ".join(item.value for item in app.markdown)
    assert "Principles of Brain-Computer Interfaces" in md_text and "Electrophysiology" in md_text
    assert "What is a Brain-Computer Interface?" in md_text
    assert "How Electroencephalography (EEG) Works" in md_text
    assert "Real BCI Systems vs. The NeuroLink Simulator" in md_text
    assert "Aditya Dugar" in md_text
    assert "25BRTSN003" in md_text
    assert "Team 2" in md_text


def test_signal_metrics_computation():
    """Verify compute_signal_metrics calculates meaningful physical statistics."""
    raw = [0.1 * (i % 5) for i in range(512)]
    filtered = [0.05 * (i % 3) for i in range(512)]
    metrics = compute_signal_metrics(raw, filtered)

    assert "vpp" in metrics
    assert "rms" in metrics
    assert "snr" in metrics
    assert "drift" in metrics
    assert "au" in metrics["vpp"]
    assert "au" in metrics["rms"]
    assert "dB" in metrics["snr"]


def test_experiment_studio_end_to_end(trained_model):
    """Verify Screen 02 (Experiment Studio) runs real simulation and produces telemetry."""
    with patch("dashboard_model.load_model", return_value=trained_model):
        app = AppTest.from_file(str(APP))
        app.query_params["page"] = "experiment-studio"
        app.run()
        assert not app.exception
        assert len(app.warning) >= 1
        assert "not live brain data" in app.warning[0].value

        # Select class "right" and process
        app.selectbox[0].select("right")
        app.number_input[0].set_value(123)
        app.button[0].click().run()

        assert not app.exception
        assert app.session_state["result"]["label"] == "right"
        assert app.session_state["result"]["seed"] == 123
        assert app.session_state["result"]["predicted"] == "right"
        assert len(app.get("plotly_chart")) == 1
