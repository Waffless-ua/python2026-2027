import re


def is_palindrome(s: str) -> bool:
    """Checks for a palindrome, ignoring case and whitespace."""
    normalized = "".join(s.casefold().split())
    return normalized == normalized[::-1]


def count_words(text: str) -> int:
    """Counts words separated by whitespace."""
    return len(text.split())


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncates text to max_len characters, including the suffix."""
    if max_len < 0:
        raise ValueError("max_len must be non-negative")

    if len(text) <= max_len:
        return text

    if len(suffix) > max_len:
        raise ValueError("suffix cannot exceed max_len when truncating")

    return text[:max_len - len(suffix)] + suffix


def to_snake_case(s: str) -> str:
    """Converts whitespace-separated words and camelCase to snake_case."""
    text = s.strip()
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    text = re.sub(r"\s+", "_", text)
    return text.lower()