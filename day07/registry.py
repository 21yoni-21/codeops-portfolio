
class BankConfig:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance


config = BankConfig()

class SMSAlert:

    def update(self, message):
        print("SMS Alert:", message)


class AuditLog:

    def update(self, message):
        print("Audit Log:", message)


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def _notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount
        self._notify(f"{self.owner} deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._notify(f"{self.owner} withdrew {amount}")
        else:
            print("Insufficient balance")

    def statement(self):
        return f"Account: {self.owner} Balance = {self.balance}"


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.rate = config.interest_rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        return f"Savings Account: {self.owner} Balance = {self.balance}"


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.overdraft = config.overdraft_limit

    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            self._notify(f"{self.owner} withdrew {amount}")
        else:
            print("Overdraft exceeded")

    def statement(self):
        return f"Current Account: {self.owner} Balance = {self.balance}"


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Unknown account type")


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(("withdraw", amount))
        else:
            print("Insufficient balance")

    def undo_last(self):

        if not self.history:
            print("No transaction")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self.balance -= amount

        elif action == "withdraw":
            self.balance += amount

        print("Undo completed")


class AccountRegistry:

    def __init__(self):
        self.by_number = {}
        self.order = []

    def add(self, acc):
        self.by_number[acc.number] = acc
        self.order.append(acc.number)

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):

        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts