import pytest

from string_utils import (
    is_palindrome,
    count_words,
    truncate,
    to_snake_case,
)


class TestIsPalindrome:
    """Groups tests for is_palindrome."""

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("", True),
            ("   ", True),
            ("a", True),
            ("Level", True),
            ("Never odd or even", True),
            ("Я несу гусеня", True),
            ("a\tb\na", True),
            ("hello", False),
            ("ab", False),
        ],
    )
    def test_is_palindrome(self, text: str, expected: bool) -> None:
        """Checks case handling, whitespace, and boundary cases."""
        result = is_palindrome(text)

        assert result is expected
        assert type(result) is bool


class TestCountWords:
    """Groups tests for count_words."""

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("", 0),
            ("   ", 0),
            ("\t\n", 0),
            ("Python", 1),
            ("Hello World", 2),
            ("  Hello   World  ", 2),
            ("one\ttwo\nthree", 3),
            ("Привіт, світе!", 2),
            ("one-two", 1),
        ],
    )
    def test_count_words(self, text: str, expected: int) -> None:
        """Checks word counting with different whitespace separators."""
        result = count_words(text)

        assert result == expected
        assert type(result) is int


class TestTruncate:
    """Groups tests for truncate."""

    @pytest.mark.parametrize(
        "text, max_len, expected",
        [
            ("", 0, ""),
            ("", 5, ""),
            ("Hi", 2, "Hi"),
            ("Hello", 5, "Hello"),
            ("Hello", 10, "Hello"),
            ("Hello World", 8, "Hello..."),
            ("Hello", 4, "H..."),
            ("Hello", 3, "..."),
        ],
    )
    def test_default_suffix(
        self,
        text: str,
        max_len: int,
        expected: str,
    ) -> None:
        """Checks truncation with the default suffix."""
        result = truncate(text, max_len)

        assert result == expected
        assert type(result) is str
        assert len(result) <= max_len

    @pytest.mark.parametrize(
        "text, max_len, suffix, expected",
        [
            ("", 0, "", ""),
            ("Hello", 0, "", ""),
            ("Hello", 3, "", "Hel"),
            ("Hello World", 6, "!", "Hello!"),
            ("Hello", 2, "..", ".."),
            ("Hello", 4, "…", "Hel…"),
            ("Hi", 2, "long suffix", "Hi"),
        ],
    )
    def test_custom_suffix(
        self,
        text: str,
        max_len: int,
        suffix: str,
        expected: str,
    ) -> None:
        """Checks custom and empty suffixes."""
        result = truncate(text, max_len, suffix)

        assert result == expected
        assert type(result) is str
        assert len(result) <= max_len

    @pytest.mark.parametrize(
        "text, max_len, suffix, message",
        [
            ("Hello", -1, "...", "max_len must be non-negative"),
            ("", -5, "", "max_len must be non-negative"),
            ("Hello", 0, "...", "suffix cannot exceed max_len"),
            ("Hello", 1, "...", "suffix cannot exceed max_len"),
            ("Hello", 2, "...", "suffix cannot exceed max_len"),
        ],
    )
    def test_invalid_arguments(
        self,
        text: str,
        max_len: int,
        suffix: str,
        message: str,
    ) -> None:
        """Checks invalid length and suffix combinations."""
        with pytest.raises(ValueError, match=message):
            truncate(text, max_len, suffix)


class TestToSnakeCase:
    """Groups tests for to_snake_case."""

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("", ""),
            ("   ", ""),
            ("a", "a"),
            ("Hello World", "hello_world"),
            ("helloWorld", "hello_world"),
            ("HelloWorld", "hello_world"),
            ("  Hello   World  ", "hello_world"),
            ("hello_world", "hello_world"),
            ("HTTPServer", "http_server"),
            ("XMLParser", "xml_parser"),
            ("Hello\tWorld\nPython", "hello_world_python"),
            ("version2Update", "version2_update"),
        ],
    )
    def test_to_snake_case(self, text: str, expected: str) -> None:
        """Checks word separation, camelCase, and acronym handling."""
        result = to_snake_case(text)

        assert result == expected
        assert type(result) is str