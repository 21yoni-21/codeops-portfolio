class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance
        self._observers = []

    @property
    def balance(self):
        return self.__balance

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount
        self._notify(f"{self.owner} deposited {amount} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        self._notify(f"{self.owner} withdrew {amount} ETB")

    def statement(self):
        return f"Account: {self.owner} - Balance: {self.balance} ETB"


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        return f"Savings Account: {self.owner} - Balance: {self.balance} ETB"


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        self._Account__balance -= amount
        self._notify(f"{self.owner} withdrew {amount} ETB")

    def statement(self):
        return f"Current Account: {self.owner} - Balance: {self.balance} ETB"


class SMSAlert:

    def update(self, message):
        print("SMS Alert:", message)


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind.lower() == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind.lower() == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Invalid account type")


sms = SMSAlert()

account1 = AccountFactory.create(
    "savings",
    "Yonas",
    "1001",
    1000
)

account2 = AccountFactory.create(
    "current",
    "Abel",
    "1002",
    500
)


account1.subscribe(sms)
account2.subscribe(sms)


account1.deposit(500)
account1.add_interest()

account2.withdraw(700)


accounts = [account1, account2]

print("\n--- Account Statements ---")

for account in accounts:
    print(account.statement())