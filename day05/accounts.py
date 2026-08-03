from account import Account


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        return f"Savings Account: {self.owner} - Balance: {self.balance}"


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self._Account__balance -= amount
        else:
            raise ValueError("Overdraft limit exceeded")

    def statement(self):
        return f"Current Account: {self.owner} - Balance: {self.balance}"