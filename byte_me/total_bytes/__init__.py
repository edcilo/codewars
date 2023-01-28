import sys


def total_bytes(object: object) -> int:
    """Return the total number of bytes in the object.

    Args:
        object (object): The object to be measured.

    Returns:
        The total number of bytes in the object.
    """
    return sys.getsizeof(object)
