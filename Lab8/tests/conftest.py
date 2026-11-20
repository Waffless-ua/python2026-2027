import pytest

from bank import BankAccount


@pytest.fixture
def account() -> BankAccount:
    """Provides a new empty account."""
    return BankAccount(pin="1234")


@pytest.fixture
def funded_account() -> BankAccount:
    """Provides an account with three transactions and a 1000 UAH balance."""
    bank_account = BankAccount(pin="1234")
    bank_account.deposit(800)
    bank_account.deposit(500)
    bank_account.withdraw(300, pin="1234")

    return bank_account