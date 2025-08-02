class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Subtract amount if sufficient funds.
        Return True if successful; False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")
