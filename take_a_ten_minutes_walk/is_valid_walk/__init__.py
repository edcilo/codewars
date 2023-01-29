def is_valid_walk(walk: list[str]) -> bool:
    """Return True if the walk return to starting point,
    False otherwise.

    Args:
        walk (list[str]): The walk to be checked.

    Returns:
        True if the walk return to starting point, False otherwise.
    """
    if len(walk) != 10:
        return False

    mapping = {
        'n': 1,
        's': -1,
        'e': 1,
        'w': -1
    }

    start = [0, 0]

    for dir in walk:
        if dir in ['n', 's']:
            start[0] += mapping[dir]
        else:
            start[1] += mapping[dir]

    return start == [0, 0]
