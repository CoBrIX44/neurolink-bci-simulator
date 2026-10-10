"""Balanced synthetic examples, processed exactly like dashboard examples."""
import numpy as np
from signal_generator import LABELS, generate_eeg
from processing import filter_eeg
from features import extract_features
from validation import validate_seed


def create_dataset(samples_per_class: int = 200, seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    if isinstance(samples_per_class, bool) or not isinstance(samples_per_class, int) or samples_per_class < 4:
        raise ValueError("samples_per_class must be an integer of at least 4.")
    validate_seed(seed)
    if seed is None:
        raise ValueError("Dataset seed must be an integer for reproducibility.")
    seeds = np.random.SeedSequence(seed).spawn(2 * samples_per_class)
    rows, labels = [], []
    for label in LABELS:
        for _ in range(samples_per_class):
            signal_seed = int(seeds[len(rows)].generate_state(1)[0])
            _, raw = generate_eeg(label, seed=signal_seed)
            rows.append(list(extract_features(filter_eeg(raw)).values()))
            labels.append(label)
    return np.asarray(rows), np.asarray(labels)
