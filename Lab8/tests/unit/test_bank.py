from decimal import Decimal
from pathlib import Path

import pytest

from bank import BankAccount


class TestBankAccount:
    """Groups tests for account operations and statements."""

    def test_initial_state(self, account: BankAccount) -> None:
        """Checks that a new account has no funds or transactions."""
        assert account.balance == Decimal("0.00")
        assert account.transactions == []
        assert isinstance(account.balance, Decimal)

    def test_funded_account(self, funded_account: BankAccount) -> None:
        """Checks the prepared balance and transaction count."""
        assert funded_account.balance == Decimal("1000.00")
        assert len(funded_account.transactions) == 3

    @pytest.mark.parametrize("amount", [1, 100, 250.50])
    def test_deposit(self, account: BankAccount, amount: int | float) -> None:
        """Checks that deposits increase the balance and create log entries."""
        account.deposit(amount)

        assert account.balance == Decimal(str(amount))
        assert account.transactions == [f"DEPOSIT: {amount:.2f} UAH"]

    @pytest.mark.parametrize("amount", [1, 250.50, 1000])
    def test_withdraw(
        self,
        funded_account: BankAccount,
        amount: int | float,
    ) -> None:
        """Checks withdrawals, including withdrawing the entire balance."""
        funded_account.withdraw(amount, pin="1234")

        assert funded_account.balance == Decimal("1000") - Decimal(str(amount))
        assert funded_account.transactions[-1] == f"WITHDRAW: {amount:.2f} UAH"
        assert len(funded_account.transactions) == 4

    @pytest.mark.parametrize("pin", ["0000", "4321", ""])
    def test_incorrect_pin(
        self,
        funded_account: BankAccount,
        pin: str,
    ) -> None:
        """Checks that an incorrect PIN leaves account data unchanged."""
        previous_transactions = funded_account.transactions

        with pytest.raises(ValueError, match="Incorrect PIN"):
            funded_account.withdraw(100, pin=pin)

        assert funded_account.balance == Decimal("1000.00")
        assert funded_account.transactions == previous_transactions

    @pytest.mark.parametrize("amount", [1000.01, 1500, 10000])
    def test_insufficient_funds(
        self,
        funded_account: BankAccount,
        amount: int | float,
    ) -> None:
        """Checks that overdraft attempts leave account data unchanged."""
        previous_transactions = funded_account.transactions

        with pytest.raises(ValueError, match="Insufficient funds"):
            funded_account.withdraw(amount, pin="1234")

        assert funded_account.balance == Decimal("1000.00")
        assert funded_account.transactions == previous_transactions

    def test_withdraw_from_empty_account(self, account: BankAccount) -> None:
        """Checks that funds cannot be withdrawn from an empty account."""
        with pytest.raises(ValueError, match="Insufficient funds"):
            account.withdraw(1, pin="1234")

        assert account.balance == Decimal("0.00")
        assert account.transactions == []

    @pytest.mark.parametrize("amount", [0, -1, -100])
    def test_invalid_deposit(
        self,
        account: BankAccount,
        amount: int,
    ) -> None:
        """Checks that non-positive deposits are rejected."""
        with pytest.raises(ValueError, match="Amount must be positive"):
            account.deposit(amount)

        assert account.balance == Decimal("0.00")
        assert account.transactions == []

    @pytest.mark.parametrize("amount", [0, -1, -100])
    def test_invalid_withdrawal(
        self,
        funded_account: BankAccount,
        amount: int,
    ) -> None:
        """Checks that non-positive withdrawals are rejected."""
        previous_transactions = funded_account.transactions

        with pytest.raises(ValueError, match="Amount must be positive"):
            funded_account.withdraw(amount, pin="1234")

        assert funded_account.balance == Decimal("1000.00")
        assert funded_account.transactions == previous_transactions

    def test_transaction_log(self, funded_account: BankAccount) -> None:
        """Checks transaction amounts and chronological order."""
        assert funded_account.transactions == [
            "DEPOSIT: 800.00 UAH",
            "DEPOSIT: 500.00 UAH",
            "WITHDRAW: 300.00 UAH",
        ]

    def test_transaction_log_is_copy(self, funded_account: BankAccount) -> None:
        """Checks that modifying a returned log does not change the account."""
        transactions = funded_account.transactions
        transactions.clear()

        assert len(funded_account.transactions) == 3

    def test_save_statement(
        self,
        funded_account: BankAccount,
        tmp_path: Path,
    ) -> None:
        """Checks that the saved statement contains transactions and balance."""
        filename = tmp_path / "statement.txt"

        funded_account.save_statement(filename)

        assert filename.is_file()
        assert filename.read_text(encoding="utf-8") == (
            "DEPOSIT: 800.00 UAH\n"
            "DEPOSIT: 500.00 UAH\n"
            "WITHDRAW: 300.00 UAH\n"
            "BALANCE: 1000.00 UAH\n"
        )

    @pytest.mark.parametrize("pin", ["", "123", "12345", "abcd", "１２３４"])
    def test_invalid_pin_format(self, pin: str) -> None:
        """Checks that invalid PIN formats are rejected."""
        with pytest.raises(
            ValueError,
            match="PIN must contain exactly four digits",
        ):
            BankAccount(pin=pin)

    @pytest.mark.parametrize("amount", [1.001, 10.555, 100.999])
    def test_invalid_amount_precision(
        self,
        account: BankAccount,
        amount: float,
    ) -> None:
        """Checks that amounts with more than two decimal places are rejected."""
        with pytest.raises(
            ValueError,
            match="Amount must have at most two decimal places",
        ):
            account.deposit(amount)

        assert account.balance == Decimal("0.00")
        assert account.transactions == []