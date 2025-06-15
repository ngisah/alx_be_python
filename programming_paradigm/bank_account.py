class BankAccount:
    """
    A simple class to represent a bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            initial_balance (float or int, optional): The starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float or int): The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float or int): The amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance to the console.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

