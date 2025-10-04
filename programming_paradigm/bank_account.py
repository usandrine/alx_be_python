# programming_paradigm/bank_account.py

class BankAccount:
    """A simple bank account class implementing basic banking operations."""

    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # private attribute for encapsulation

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance is available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance}")
