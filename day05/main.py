class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

    def statement(self):
        print("Account Type: Account")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self._balance, "ETB")


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self._balance * self.rate
        self._balance += interest

    def statement(self):
        print("Account Type: Savings Account")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self._balance, "ETB")
        print("Interest Rate:", self.rate)


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0, overdraft=500):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount

    def statement(self):
        print("Account Type: Current Account")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self._balance, "ETB")
        print("Overdraft Limit:", self.overdraft, "ETB")


savings = SavingsAccount("Yonas", "1001", 1000, 0.05)
current = CurrentAccount("Abel", "1002", 500, 300)
account = Account("Sara", "1003", 700)

savings.deposit(500)
savings.add_interest()

current.withdraw(700)

account.deposit(200)

accounts = [savings, current, account]

for acc in accounts:
    acc.statement()
    print()