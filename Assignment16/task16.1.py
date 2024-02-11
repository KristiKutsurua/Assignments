class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

account1 = BankAccount("123456", "Mariami", 1000.0)
account2 = BankAccount("789012", "Giorgi", 500.0)

account1.deposit(500)
account1.withdraw(200)

account2.deposit(1000)
account2.withdraw(700)
