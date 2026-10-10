"""Offline filtering uses future samples and does not remove all artifacts."""
import numpy as np
from scipy.signal import butter, sosfiltfilt
from validation import positive_number, signal_array


def filter_eeg(signal, sampling_rate: float = 256) -> np.ndarray:
    values = signal_array(signal)
    rate = positive_number(sampling_rate, "sampling_rate")
    if rate <= 80:
        raise ValueError("sampling_rate must exceed 80 Hz for the 40 Hz cutoff.")
    sos = butter(4, [1, 40], btype="bandpass", fs=rate, output="sos")
    try:
        result = sosfiltfilt(sos, values)
    except ValueError as exc:
        raise ValueError("Signal is too short for offline filtering; provide at least 28 samples.") from exc
    if not np.isfinite(result).all():
        raise ValueError("Filtering produced non-finite values; reduce signal amplitude.")
    return result
