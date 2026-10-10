"""Generate artificial EEG-like signals; never electrode recordings."""
import numpy as np
from validation import positive_number, validate_seed

LABELS = ("left", "right")


def generate_eeg(label: str, duration: float = 2.0, sampling_rate: float = 256,
                 seed: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Return seconds and arbitrary amplitudes with deliberately separable patterns."""
    if label not in LABELS:
        raise ValueError("label must be 'left' or 'right' (artificial categories).")
    duration = positive_number(duration, "duration")
    sampling_rate = positive_number(sampling_rate, "sampling_rate")
    if sampling_rate <= 120:
        raise ValueError("sampling_rate must exceed 120 Hz to represent the 60 Hz noise component.")
    count = duration * sampling_rate
    if not np.isfinite(count) or not 2 <= count <= 1_000_000 or not np.isclose(count, round(count), atol=1e-8, rtol=0):
        raise ValueError("duration × sampling_rate must be an integer between 2 and 1,000,000 samples.")
    validate_seed(seed)
    rng = np.random.default_rng(seed)
    time = np.arange(round(count)) / sampling_rate
    dominant, secondary = ((8, 22) if label == "left" else (22, 8))
    phases = rng.uniform(0, 2 * np.pi, 4)
    signal = (rng.uniform(1.4, 2.0) * np.sin(2 * np.pi * dominant * time + phases[0])
              + rng.uniform(.2, .5) * np.sin(2 * np.pi * secondary * time + phases[1])
              + .4 * np.sin(2 * np.pi * .3 * time + phases[2])
              + .25 * np.sin(2 * np.pi * 60 * time + phases[3])
              + rng.normal(0, .45, time.size))
    return time, signal
