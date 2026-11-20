import pytest

from validators import (
    validate_email,
    validate_phone,
    validate_password,
    validate_date,
)


class TestValidateEmail:
    """Groups email validation tests."""

    @pytest.mark.parametrize(
        "email",
        [
            "user@example.com",
            "john.doe@example.org",
            "user+tag@example.com",
            "user_name@example.net",
            "user123@sub.example.com",
            "USER@EXAMPLE.COM",
            "a@b.co",
            "user@my-domain.com",
        ],
    )
    def test_valid_email(self, email: str) -> None:
        """Checks valid email formats."""
        assert validate_email(email) is True

    @pytest.mark.parametrize(
        "email",
        [
            "",
            "userexample.com",
            "user@",
            "@example.com",
            "user@example",
            "user name@example.com",
            ".user@example.com",
            "user..name@example.com",
            "user@-example.com",
            "user@example.com\n",
        ],
    )
    def test_invalid_email(self, email: str) -> None:
        """Checks malformed and incomplete email addresses."""
        assert validate_email(email) is False


class TestValidatePhone:
    """Groups Ukrainian phone validation tests."""

    @pytest.mark.parametrize(
        "phone",
        [
            "0671234567",
            "0509876543",
            "+380671234567",
            "+380509876543",
            "+38(067)1234567",
            "(067)1234567",
            "067-123-45-67",
            "067 123 45 67",
            "+38(067) 123 45 67",
            "+38067-123-45-67",
        ],
    )
    def test_valid_phone(self, phone: str) -> None:
        """Checks supported Ukrainian phone formats."""
        assert validate_phone(phone) is True

    @pytest.mark.parametrize(
        "phone",
        [
            "",
            "067123456",
            "06712345678",
            "1671234567",
            "+480671234567",
            "067ABC4567",
            "(0671234567",
            "067)1234567",
            "067-123 45-67",
            "0671234567\n",
        ],
    )
    def test_invalid_phone(self, phone: str) -> None:
        """Checks invalid lengths, prefixes, and separators."""
        assert validate_phone(phone) is False


class TestValidatePassword:
    """Groups password validation tests."""

    @pytest.mark.parametrize(
        "password",
        [
            "Abcdef1!",
            "Password1@",
            "HELLO123#",
            "StrongPwd9$",
            "My_pass8",
            "Qwerty77%",
            "Test2026&",
            "A1!aaaaa",
        ],
    )
    def test_valid_password(self, password: str) -> None:
        """Checks passwords satisfying every requirement."""
        assert validate_password(password) == {
            "valid": True,
            "errors": [],
        }

    @pytest.mark.parametrize(
        "password, expected_errors",
        [
            (
                "",
                [
                    "Password must contain at least 8 characters",
                    "Password must contain an uppercase letter",
                    "Password must contain a digit",
                    "Password must contain a special character",
                ],
            ),
            (
                "Aa1!",
                ["Password must contain at least 8 characters"],
            ),
            (
                "abcdef1!",
                ["Password must contain an uppercase letter"],
            ),
            (
                "Abcdefg!",
                ["Password must contain a digit"],
            ),
            (
                "Abcdef12",
                ["Password must contain a special character"],
            ),
            (
                "abcdefgh",
                [
                    "Password must contain an uppercase letter",
                    "Password must contain a digit",
                    "Password must contain a special character",
                ],
            ),
            (
                "12345678",
                [
                    "Password must contain an uppercase letter",
                    "Password must contain a special character",
                ],
            ),
            (
                "ABCDEFGH",
                [
                    "Password must contain a digit",
                    "Password must contain a special character",
                ],
            ),
            (
                "Abcdef1 ",
                ["Password must contain a special character"],
            ),
        ],
    )
    def test_invalid_password(
        self,
        password: str,
        expected_errors: list[str],
    ) -> None:
        """Checks rejection and the exact list of failed requirements."""
        assert validate_password(password) == {
            "valid": False,
            "errors": expected_errors,
        }


class TestValidateDate:
    """Groups date validation tests."""

    @pytest.mark.parametrize(
        "date_text",
        [
            "01.01.2026",
            "31.12.2026",
            "29.02.2024",
            "29.02.2000",
            "28.02.1900",
            "30.04.2026",
            "01.01.0001",
            "31.12.9999",
        ],
    )
    def test_valid_date(self, date_text: str) -> None:
        """Checks real dates, leap years, and year boundaries."""
        assert validate_date(date_text) is True

    @pytest.mark.parametrize(
        "date_text",
        [
            "",
            "1.01.2026",
            "01.1.2026",
            "2026-01-01",
            "31.04.2026",
            "29.02.2025",
            "29.02.1900",
            "00.01.2026",
            "01.13.2026",
            "01.01.0000",
            "01.01.2026\n",
        ],
    )
    def test_invalid_date(self, date_text: str) -> None:
        """Checks malformed dates and impossible calendar values."""
        assert validate_date(date_text) is False


@pytest.mark.slow
class TestLargeDatasets:
    """Groups validation tests using large generated datasets."""

    @pytest.mark.parametrize("size", [10_000, 20_000])
    def test_email_dataset(self, size: int) -> None:
        """Checks large sets of valid and invalid email addresses."""
        for index in range(size):
            assert validate_email(f"user{index}@example.com") is True
            assert validate_email(f"user{index}example.com") is False

    @pytest.mark.parametrize("size", [10_000, 20_000])
    def test_phone_dataset(self, size: int) -> None:
        """Checks large sets of valid and oversized phone numbers."""
        for index in range(size):
            phone = f"067{index:07d}"

            assert validate_phone(phone) is True
            assert validate_phone(phone + "0") is False

    @pytest.mark.parametrize("size", [10_000, 20_000])
    def test_password_dataset(self, size: int) -> None:
        """Checks large sets of passwords with and without uppercase letters."""
        for index in range(size):
            assert validate_password(f"Password{index}!")["valid"] is True
            assert validate_password(f"password{index}!")[
                "valid"
            ] is False

    @pytest.mark.parametrize("year_start", [1900, 2000])
    def test_date_dataset(self, year_start: int) -> None:
        """Checks valid month starts and invalid day numbers across 100 years."""
        for year in range(year_start, year_start + 100):
            for month in range(1, 13):
                assert validate_date(f"01.{month:02d}.{year}") is True
                assert validate_date(f"32.{month:02d}.{year}") is False