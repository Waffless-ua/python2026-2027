from math import isqrt, isnan


def factorial(n: int) -> int:
    """Returns the factorial of a non-negative integer."""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 1

    return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """Returns whether an integer is prime."""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 2:
        raise ValueError("n must be at least 2")

    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False

    return True


def gcd(a: int, b: int) -> int:
    """Returns the non-negative greatest common divisor of two integers."""
    if type(a) is not int or type(b) is not int:
        raise TypeError("Both arguments must be integers")

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def clamp(
    value: int | float,
    lo: int | float,
    hi: int | float,
) -> int | float:
    """Clamps a numeric value to the inclusive range [lo, hi]."""
    for name, number in (("value", value), ("lo", lo), ("hi", hi)):
        if type(number) not in (int, float):
            raise TypeError(f"{name} must be an integer or a float")
        if isinstance(number, float) and isnan(number):
            raise ValueError(f"{name} cannot be NaN")

    if lo > hi:
        raise ValueError("Lower bound cannot exceed upper bound")

    if value < lo:
        return lo
    if value > hi:
        return hi
    return value