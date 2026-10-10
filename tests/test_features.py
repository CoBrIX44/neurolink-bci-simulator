import numpy as np
import pytest
from features import FEATURE_NAMES, extract_features


@pytest.mark.parametrize("hz, index", [(8, 0), (12, 1), (22, 1), (40, 1)])
def test_known_sine_and_boundary(hz, index):
    t = np.arange(512) / 256
    result = extract_features(np.sin(2*np.pi*hz*t) + 17)
    assert tuple(result) == FEATURE_NAMES
    values = list(result.values())
    # Squared normalized magnitude of a unit sine is 1/4 at its positive bin.
    assert values[index] == pytest.approx(.25 / (22 if index == 0 else 57))
    assert values[1-index] < 1e-25


def test_constant_and_empty_bins():
    assert list(extract_features(np.ones(512)).values()) == [0, 0]
    with pytest.raises(ValueError, match="No FFT bins"):
        extract_features([1, 2])


@pytest.mark.parametrize("x", [[], [[1, 2]], [1, np.nan], [1j, 2j]])
def test_invalid(x):
    with pytest.raises(ValueError):
        extract_features(x)
