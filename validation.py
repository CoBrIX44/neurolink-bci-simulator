"""Shared validation for the educational, one-channel offline pipeline."""
import numpy as np


def positive_number(value: float, name: str) -> float:
    if isinstance(value, (bool, str)):
        raise ValueError(f"{name} must be a positive finite number.")
    try:
        value = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a positive finite number.") from exc
    if not np.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a positive finite number.")
    return value


def validate_seed(seed: int | None) -> None:
    if seed is not None and (isinstance(seed, bool) or not isinstance(seed, (int, np.integer)) or seed < 0):
        raise ValueError("seed must be a non-negative integer or None.")


def signal_array(signal) -> np.ndarray:
    try:
        if np.iscomplexobj(signal):
            raise ValueError("Complex signals are unsupported.")
        values = np.asarray(signal, dtype=float)
    except (ValueError, TypeError) as exc:
        raise ValueError("Signal must be a real numeric one-dimensional array.") from exc
    if values.ndim != 1 or values.size < 2 or not np.isfinite(values).all():
        raise ValueError("Signal must be one-dimensional with at least two finite samples.")
    return values
