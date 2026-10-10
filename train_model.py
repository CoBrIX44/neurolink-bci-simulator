"""Train and evaluate only on generated signals, never real EEG."""
import json
from pathlib import Path
import joblib
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from dataset import create_dataset
from features import FEATURE_NAMES
from model_utils import MODEL_PATH


def train_model(path: Path | str | None = MODEL_PATH, samples_per_class: int = 200, seed: int = 42):
    """Train on synthetic data; path=None returns an in-memory model without writing files."""
    X, y = create_dataset(samples_per_class, seed)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.25, random_state=seed, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(random_state=seed, max_iter=1000))
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    metrics = {
        "scope": "SYNTHETIC DATA ONLY — not real EEG or human-intention performance",
        "seed": seed, "train_examples": len(y_train), "test_examples": len(y_test),
        "test_class_counts": {label: int(sum(y_test == label)) for label in model.classes_},
        "accuracy": accuracy_score(y_test, predicted),
        "confusion_matrix_labels": list(model.classes_),
        "confusion_matrix": confusion_matrix(y_test, predicted, labels=model.classes_).tolist(),
        "classification_report": classification_report(y_test, predicted, output_dict=True, zero_division=0),
    }
    if path is None:
        return model, metrics
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    artifact = {"schema_version": 1, "feature_names": FEATURE_NAMES, "pipeline": model,
                "sklearn_version": sklearn.__version__, "metrics": metrics}
    temporary = path.with_suffix(".tmp")
    joblib.dump(artifact, temporary)
    temporary.replace(path)
    path.with_suffix(".metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return model, metrics


if __name__ == "__main__":
    _, report = train_model()
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"Saved local model: {MODEL_PATH}")
