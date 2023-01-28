from typing import Union

def multiply(
    a: Union[int, float, complex],
    b: Union[int, float, complex]
    ) -> Union[int, float, complex]:
    """Multiply two numbers together.

    Args:
        a (int, float, complex): The first number.
        b (int, float, complex): The second number.

    Returns:
        The product of the two numbers.
    """
    return a * b
