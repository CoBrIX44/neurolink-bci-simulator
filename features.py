"""Two mean squared-amplitude FFT features with an explicit band convention."""
import numpy as np
from validation import positive_number, signal_array

FEATURE_NAMES = ("mean_power_1_12_hz", "mean_power_12_40_hz")


def extract_features(signal, sampling_rate: float = 256) -> dict[str, float]:
    """Mean |rFFT(x-mean(x))/N|² per bin; [1,12), [12,40] Hz.

    This is not a PSD or integrated band power; units are arbitrary amplitude².
    The 12 Hz bin belongs only to the second band.
    """
    values = signal_array(signal)
    rate = positive_number(sampling_rate, "sampling_rate")
    if rate <= 80:
        raise ValueError("sampling_rate must exceed 80 Hz to cover both feature bands.")
    frequencies = np.fft.rfftfreq(values.size, 1 / rate)
    power = np.abs(np.fft.rfft(values - values.mean()) / values.size) ** 2
    masks = ((frequencies >= 1) & (frequencies < 12),
             (frequencies >= 12) & (frequencies <= 40))
    features = {}
    for name, mask in zip(FEATURE_NAMES, masks):
        if not mask.any():
            raise ValueError(f"No FFT bins for {name}; increase signal duration.")
        features[name] = float(power[mask].mean())
    if not np.isfinite(list(features.values())).all():
        raise ValueError("Feature power is non-finite; reduce signal amplitude.")
    return features
