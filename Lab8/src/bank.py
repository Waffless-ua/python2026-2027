from decimal import Decimal
from pathlib import Path


class BankAccount:
    """Represents a bank account with PIN protection and a transaction log."""

    def __init__(self, pin: str) -> None:
        """Creates an empty account with a four-digit PIN."""
        if len(pin) != 4 or not pin.isascii() or not pin.isdigit():
            raise ValueError("PIN must contain exactly four digits")

        self.__pin = pin
        self._balance = Decimal("0.00")
        self._transactions: list[str] = []

    @property
    def balance(self) -> Decimal:
        """Returns the current balance."""
        return self._balance

    @property
    def transactions(self) -> list[str]:
        """Returns a copy of the transaction log."""
        return self._transactions.copy()

    @staticmethod
    def _validate_amount(amount: int | float | Decimal) -> Decimal:
        """Validates a positive amount with at most two decimal places."""
        value = Decimal(str(amount))

        if not value.is_finite() or value <= 0:
            raise ValueError("Amount must be positive and finite")

        if value != value.quantize(Decimal("0.01")):
            raise ValueError("Amount must have at most two decimal places")

        return value

    def deposit(self, amount: int | float | Decimal) -> None:
        """Deposits a positive amount and records the transaction."""
        value = self._validate_amount(amount)

        self._balance += value
        self._transactions.append(f"DEPOSIT: {value:.2f} UAH")

    def withdraw(self, amount: int | float | Decimal, pin: str) -> None:
        """Withdraws funds after checking the PIN and available balance."""
        if pin != self.__pin:
            raise ValueError("Incorrect PIN")

        value = self._validate_amount(amount)

        if value > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= value
        self._transactions.append(f"WITHDRAW: {value:.2f} UAH")

    def save_statement(self, filename: str | Path) -> None:
        """Writes the transaction log and current balance to a UTF-8 file."""
        with open(filename, "w", encoding="utf-8") as file:
            for transaction in self._transactions:
                file.write(transaction + "\n")

            file.write(f"BALANCE: {self._balance:.2f} UAH\n")

