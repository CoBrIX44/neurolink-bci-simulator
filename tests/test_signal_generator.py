import numpy as np
import pytest
from signal_generator import generate_eeg


@pytest.mark.parametrize("label", ["left", "right"])
def test_default_and_repeatability(label):
    t, x = generate_eeg(label, seed=9)
    assert x.shape == t.shape == (512,)
    assert t[0] == 0 and t[-1] == 511 / 256
    np.testing.assert_allclose(np.diff(t), 1 / 256)
    np.testing.assert_array_equal(x, generate_eeg(label, seed=9)[1])
    assert np.isfinite(x).all()
    assert not np.array_equal(x, generate_eeg(label, seed=10)[1])


@pytest.mark.parametrize("kwargs", [dict(label="up"), dict(duration=0), dict(duration=float("nan")),
    dict(duration=.001), dict(sampling_rate=80), dict(sampling_rate=True), dict(seed=-1), dict(seed=1.2)])
def test_invalid(kwargs):
    with pytest.raises(ValueError):
        generate_eeg(**({"label": "left"} | kwargs))
