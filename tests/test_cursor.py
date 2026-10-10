import pytest
from cursor import move_cursor


@pytest.mark.parametrize("start, command, expected", [(50, "left", 40), (50, "right", 60),
    (0, "left", 0), (100, "right", 100), (5, "left", 0), (95, "right", 100)])
def test_movement_and_bounds(start, command, expected):
    assert move_cursor(start, command) == expected


@pytest.mark.parametrize("position,command", [(-1, "left"), (101, "right"), (True, "left"),
    (1.5, "right"), (50, "up")])
def test_invalid(position, command):
    with pytest.raises(ValueError):
        move_cursor(position, command)
