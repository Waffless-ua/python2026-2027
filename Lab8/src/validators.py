import re
from datetime import datetime
from string import punctuation


def validate_email(email: str) -> bool:
    """Checks a basic email format without verifying mailbox existence."""
    pattern = (
        r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*@"
        r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
        r"[A-Za-z]{2,}"
    )
    return re.fullmatch(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    """Checks supported Ukrainian phone formats."""
    pattern = (
        r"(?:\+38)?"
        r"(?:0[0-9]{2}|\(0[0-9]{2}\))"
        r"(?:[0-9]{7}| [0-9]{3} [0-9]{2} [0-9]{2}"
        r"|[0-9]{3}-[0-9]{2}-[0-9]{2}"
        r"|-[0-9]{3}-[0-9]{2}-[0-9]{2})"
    )
    return re.fullmatch(pattern, phone) is not None


def validate_password(pwd: str) -> dict[str, bool | list[str]]:
    """Checks password length, uppercase letters, digits, and special symbols."""
    errors: list[str] = []

    if len(pwd) < 8:
        errors.append("Password must contain at least 8 characters")

    if not any(character.isupper() for character in pwd):
        errors.append("Password must contain an uppercase letter")

    if not any(character.isdigit() for character in pwd):
        errors.append("Password must contain a digit")

    if not any(character in punctuation for character in pwd):
        errors.append("Password must contain a special character")

    return {
        "valid": not errors,
        "errors": errors,
    }


def validate_date(s: str) -> bool:
    """Checks the DD.MM.YYYY format and whether the date exists."""
    if re.fullmatch(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}", s) is None:
        return False

    try:
        datetime.strptime(s, "%d.%m.%Y")
    except ValueError:
        return False

    return True