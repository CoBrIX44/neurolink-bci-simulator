import joblib
from unittest.mock import patch
import numpy as np
import pytest
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from dataset import create_dataset
from train_model import train_model
from model_utils import load_model, predict_command, MODEL_PATH
from features import extract_features
from processing import filter_eeg
from signal_generator import generate_eeg


def test_dataset_balance_and_reproducibility():
    X, y = create_dataset(12, 31)
    second = create_dataset(12, 31)
    assert X.shape == (24, 2)
    assert dict(zip(*np.unique(y, return_counts=True))) == {"left": 12, "right": 12}
    np.testing.assert_array_equal(X, second[0])
    np.testing.assert_array_equal(y, second[1])
    assert not np.array_equal(X, create_dataset(12, 32)[0])


def test_train_load_predict_and_cwd(tmp_path, monkeypatch):
    path = tmp_path / "model.joblib"
    trained, report = train_model(path, 40)
    assert isinstance(trained[0], StandardScaler)
    assert isinstance(trained[-1], LogisticRegression)
    assert trained[0].n_samples_seen_ == 60
    assert report["test_class_counts"] == {"left": 10, "right": 10}
    assert report["accuracy"] >= .9  # Only tests this deliberately separable synthetic generator.
    assert "SYNTHETIC DATA ONLY" in report["scope"]
    assert path.with_suffix(".metrics.json").exists()
    monkeypatch.chdir(tmp_path)
    assert MODEL_PATH.is_absolute()
    restored = load_model(path)
    for label in ("left", "right"):
        features = extract_features(filter_eeg(generate_eeg(label, seed=12345)[1]))
        command, scores = predict_command(restored, dict(reversed(list(features.items()))))
        assert command == label
        assert set(scores) == {"left", "right"}
        assert sum(scores.values()) == pytest.approx(1)
        assert predict_command(trained, features) == (command, scores)
    other, second_report = train_model(tmp_path / "second.joblib", 40)
    np.testing.assert_array_equal(trained[-1].coef_, other[-1].coef_)
    assert report == second_report


def test_missing_corrupt_and_schema(tmp_path):
    with pytest.raises(FileNotFoundError, match="train_model.py"):
        load_model(tmp_path / "missing")
    path = tmp_path / "broken"
    path.write_text("broken")
    with pytest.raises(ValueError, match="train_model.py"):
        load_model(path)
    joblib.dump({"schema_version": 0}, path)
    with pytest.raises(ValueError, match="incompatible"):
        load_model(path)


@pytest.mark.parametrize("count", [0, -1, 3, True, 1.2])
def test_invalid_dataset(count):
    with pytest.raises(ValueError):
        create_dataset(count)


def test_invalid_inference():
    with pytest.raises(ValueError, match="Expected features"):
        predict_command(None, {"wrong": 1})
    with pytest.raises(ValueError, match="finite"):
        predict_command(None, {"mean_power_1_12_hz": np.nan, "mean_power_12_40_hz": 2})


def test_in_memory_training_does_not_write_files(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with patch("train_model.joblib.dump") as dump:
        model, report = train_model(path=None, samples_per_class=8)
        assert list(model.classes_) == ["left", "right"]
        assert report["test_examples"] == 4
        dump.assert_not_called()
    assert list(tmp_path.iterdir()) == []
