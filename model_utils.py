"""Project-relative, local model persistence and checked inference."""
from pathlib import Path
import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from features import FEATURE_NAMES

PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "models" / "neurolink.joblib"
TRAIN_HELP = "Run python train_model.py from the project folder, then try again."


def load_model(path: Path | str = MODEL_PATH) -> Pipeline:
    """Load only trusted, locally trained joblib files (pickle is executable)."""
    if not Path(path).is_file():
        raise FileNotFoundError(f"Model missing at {path}. {TRAIN_HELP}")
    try:
        artifact = joblib.load(path)
        if artifact["schema_version"] != 1 or tuple(artifact["feature_names"]) != FEATURE_NAMES:
            raise ValueError("Unsupported model schema.")
        model = artifact["pipeline"]
        if not isinstance(model, Pipeline) or not isinstance(model[0], StandardScaler) or not isinstance(model[-1], LogisticRegression):
            raise ValueError("Unexpected model pipeline.")
        if list(model.classes_) != ["left", "right"] or model.n_features_in_ != 2:
            raise ValueError("Unexpected model classes or features.")
        return model
    except Exception as exc:
        raise ValueError(f"Model is unreadable or incompatible. {TRAIN_HELP}") from exc


def predict_command(model: Pipeline, features: dict[str, float]) -> tuple[str, dict[str, float]]:
    if set(features) != set(FEATURE_NAMES):
        raise ValueError(f"Expected features: {', '.join(FEATURE_NAMES)}.")
    row = np.asarray([[features[name] for name in FEATURE_NAMES]], dtype=float)
    if not np.isfinite(row).all() or (row < 0).any():
        raise ValueError("Feature values must be finite, non-negative powers.")
    scores = model.predict_proba(row)[0]
    if not np.isfinite(scores).all():
        raise ValueError("Model produced invalid scores. " + TRAIN_HELP)
    return str(model.predict(row)[0]), dict(zip(model.classes_, map(float, scores)))
