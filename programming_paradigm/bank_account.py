# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Private balance

    def deposit(self, amount):
        self.__account_balance += amount  # Add money

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount  # Remove money
            return True
        return False  # Not enough money

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
  # Show balance
