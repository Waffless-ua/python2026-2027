import math

import pytest

from math_utils import factorial, is_prime, gcd, clamp


class TestFactorial:
    """Groups tests for the factorial function."""

    @pytest.mark.parametrize(
        "n, expected",
        [
            (3, 6),
            (5, 120),
            (7, 5040),
        ],
    )
    def test_factorial_normal(self, n: int, expected: int) -> None:
        """Checks factorial values for positive integers."""
        result = factorial(n)

        assert result == expected
        assert type(result) is int

    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 1),
            (1, 1),
        ],
    )
    def test_factorial_boundaries(self, n: int, expected: int) -> None:
        """Checks the zero and one boundary cases."""
        result = factorial(n)

        assert result == expected
        assert type(result) is int

    @pytest.mark.parametrize("n", [-1, -5, -100])
    def test_factorial_negative(self, n: int) -> None:
        """Checks that negative integers raise ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            factorial(n)

    @pytest.mark.parametrize("n", [2.5, 5.0, "5", None, True, False])
    def test_factorial_invalid_type(self, n: object) -> None:
        """Checks that noninteger arguments raise TypeError."""
        with pytest.raises(TypeError, match="n must be an integer"):
            factorial(n)

    def test_factorial_large(self) -> None:
        """Checks a large factorial against the standard library."""
        result = factorial(100)

        assert result == math.factorial(100)
        assert type(result) is int



class TestIsPrime:
    """Groups tests for the is_prime function."""

    @pytest.mark.parametrize(
        "n, expected",
        [
            (3, True),
            (10007, True),
            (67, True),
            (66, False),
            (4, False),
            (12, False),
        ],
    )
    def test_is_prime_normal(self, n: int, expected: bool) -> None:
        """Checks prime and composite numbers."""
        result = is_prime(n)

        assert result is expected
        assert type(result) is bool

    @pytest.mark.parametrize(
        "n, expected",
        [
            (2, True),
            (49, False),
            (121, False),
        ],
    )
    def test_is_prime_boundaries(self, n: int, expected: bool) -> None:
        """Checks the smallest prime and squares of prime numbers."""
        result = is_prime(n)

        assert result is expected
        assert type(result) is bool

    @pytest.mark.parametrize("n", [0, 1, -1, -2443242])
    def test_is_prime_below_two(self, n: int) -> None:
        """Checks that integers below two raise ValueError."""
        with pytest.raises(ValueError, match="n must be at least 2"):
            is_prime(n)

    @pytest.mark.parametrize("n", [2.5, 5.0, "5", None, True, False])
    def test_is_prime_invalid_type(self, n: object) -> None:
        """Checks that noninteger arguments raise TypeError."""
        with pytest.raises(TypeError, match="n must be an integer"):
            is_prime(n)

    @pytest.mark.parametrize(
        "n, expected",
        [
            (2147483647, True),
            (10**100, False),
        ],
    )
    def test_is_prime_large(self, n: int, expected: bool) -> None:
        """Checks a large prime and a very large even number."""
        result = is_prime(n)

        assert result is expected
        assert type(result) is bool


class TestGcd:
    """Groups tests for the gcd function."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (12, 18, 6),
            (48, 18, 6),
            (17, 13, 1),
        ],
    )
    def test_gcd_normal(self, a: int, b: int, expected: int) -> None:
        """Checks common divisors and coprime arguments."""
        result = gcd(a, b)

        assert result == expected
        assert type(result) is int

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (0, 0, 0),
            (0, 5, 5),
            (5, 0, 5),
            (1, 10, 1),
            (10, 1, 1),
            (7, 7, 7),
            (-12, 18, 6),
            (12, -18, 6),
            (-12, -18, 6),
        ],
    )
    def test_gcd_boundaries(self, a: int, b: int, expected: int) -> None:
        """Checks zero, one, equal numbers, and negative arguments."""
        result = gcd(a, b)

        assert result == expected
        assert type(result) is int

    @pytest.mark.parametrize(
        "a, b",
        [
            (2.5, 5),
            (5, 2.5),
            ("5", 10),
            (10, "5"),
            (None, 5),
            (5, None),
            (True, 5),
            (5, False),
        ],
    )
    def test_gcd_invalid_type(self, a: object, b: object) -> None:
        """Checks invalid types in either argument."""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            gcd(a, b)

    def test_gcd_large(self) -> None:
        """Checks the greatest common divisor of very large integers."""
        result = gcd(12 * 10**100, 18 * 10**100)

        assert result == 6 * 10**100
        assert type(result) is int


class TestClamp:
    """Groups tests for the clamp function."""

    @pytest.mark.parametrize(
        "value, lo, hi, expected",
        [
            (-5, 0, 10, 0),
            (5, 0, 10, 5),
            (15, 0, 10, 10),
            (2.5, 0.0, 5.0, 2.5),
            (-1.5, 0.0, 5.0, 0.0),
            (8.5, 0.0, 5.0, 5.0),
        ],
    )
    def test_clamp_normal(
        self,
        value: int | float,
        lo: int | float,
        hi: int | float,
        expected: int | float,
    ) -> None:
        """Checks values below, within, and above the range."""
        result = clamp(value, lo, hi)

        assert result == expected
        assert type(result) is type(expected)

    @pytest.mark.parametrize(
        "value, lo, hi, expected",
        [
            (0, 0, 10, 0),
            (10, 0, 10, 10),
            (1, 0, 1, 1),
            (0, 0, 0, 0),
            (-5, -10, -1, -5),
            (-20, -10, -1, -10),
            (0, -10, -1, -1),
            (3, 5, 5, 5),
            (7, 5, 5, 5),
            (10**100, 0, 10**50, 10**50),
            (-10**100, -10**50, 0, -10**50),
        ],
    )
    def test_clamp_boundaries(
        self,
        value: int | float,
        lo: int | float,
        hi: int | float,
        expected: int | float,
    ) -> None:
        """Checks endpoints, equal bounds, negatives, and large integers."""
        result = clamp(value, lo, hi)

        assert result == expected
        assert type(result) is type(expected)

    @pytest.mark.parametrize(
        "value, lo, hi",
        [
            (5, 10, 0),
            (0, 1, -1),
            (2.5, 5.0, 1.0),
        ],
    )
    def test_clamp_invalid_bounds(
        self,
        value: int | float,
        lo: int | float,
        hi: int | float,
    ) -> None:
        """Checks that reversed bounds raise ValueError."""
        with pytest.raises(
            ValueError,
            match="Lower bound cannot exceed upper bound",
        ):
            clamp(value, lo, hi)

    @pytest.mark.parametrize(
        "value, lo, hi, argument",
        [
            ("5", 0, 10, "value"),
            (5, "0", 10, "lo"),
            (5, 0, "10", "hi"),
            (None, 0, 10, "value"),
            (5, None, 10, "lo"),
            (5, 0, None, "hi"),
            (True, 0, 10, "value"),
            (5, False, 10, "lo"),
            (5, 0, True, "hi"),
        ],
    )
    def test_clamp_invalid_type(
        self,
        value: object,
        lo: object,
        hi: object,
        argument: str,
    ) -> None:
        """Checks invalid types in each argument."""
        with pytest.raises(
            TypeError,
            match=f"{argument} must be an integer or a float",
        ):
            clamp(value, lo, hi)

    @pytest.mark.parametrize(
        "value, lo, hi, argument",
        [
            (float("nan"), 0, 10, "value"),
            (5, float("nan"), 10, "lo"),
            (5, 0, float("nan"), "hi"),
        ],
    )
    def test_clamp_nan(
        self,
        value: int | float,
        lo: int | float,
        hi: int | float,
        argument: str,
    ) -> None:
        """Checks that NaN is rejected in every argument."""
        with pytest.raises(ValueError, match=f"{argument} cannot be NaN"):
            clamp(value, lo, hi)