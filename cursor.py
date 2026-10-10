"""Optional bounded cursor simulation, not physical device control."""


def move_cursor(position: int, command: str) -> int:
    if isinstance(position, bool) or not isinstance(position, int) or not 0 <= position <= 100:
        raise ValueError("Cursor position must be an integer in [0,100].")
    if command not in ("left", "right"):
        raise ValueError("Simulated cursor command must be left or right.")
    return max(0, min(100, position + (-10 if command == "left" else 10)))
