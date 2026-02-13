"""
Example of __init__ constructor and instance variables
"""

class BankAccount:
    """Represents a simple bank account"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money if sufficient balance"""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def display(self):
        """Displays account information"""
        print(f"Owner: {self.owner}, Balance: {self.balance}")


if __name__ == "__main__":
    account = BankAccount("Dinara", 100)
    account.deposit(50)
    account.withdraw(30)
    account.display()
