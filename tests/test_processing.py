import numpy as np
import pytest
from processing import filter_eeg
from signal_generator import generate_eeg


def test_shape_and_spectral_attenuation():
    t, x = generate_eeg("left", seed=3)
    y = filter_eeg(x)
    assert y.shape == x.shape and np.isfinite(y).all()
    t = np.arange(2560) / 256
    raw = np.sin(2*np.pi*8*t) + np.sin(2*np.pi*60*t)
    filtered = filter_eeg(raw)[256:-256]
    middle = t[256:-256]
    amplitude = lambda hz: abs(2 * np.mean(filtered * np.exp(-2j*np.pi*hz*middle)))
    assert .9 < amplitude(8) < 1.1
    assert amplitude(60) < .1


@pytest.mark.parametrize("x", [[], [1], [1]*20, [[1, 2]], [1, float("nan")], [1, float("inf")], [1j, 2j]])
def test_invalid_signal(x):
    with pytest.raises(ValueError):
        filter_eeg(x)


@pytest.mark.parametrize("rate", [0, 80, -1, float("nan")])
def test_invalid_rate(rate):
    with pytest.raises(ValueError):
        filter_eeg(np.ones(512), rate)
