def is_prime(n: int) -> bool:
    """Check if a natural positive number is prime.

    Args:
        n (int): The number to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
