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
        self.history = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def _notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):

        self.balance += amount

        self.history.append({
            "type": "deposit",
            "amount": amount
        })

        self._notify(f"{self.owner} deposited {amount}")

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            self.history.append({
                "type": "withdraw",
                "amount": amount
            })

            self._notify(f"{self.owner} withdrew {amount}")

        else:
            print("Insufficient balance")

    def undo_last(self):

        if not self.history:
            print("No transaction history")
            return

        transaction = self.history.pop()

        if transaction["type"] == "deposit":
            self.balance -= transaction["amount"]

        elif transaction["type"] == "withdraw":
            self.balance += transaction["amount"]

        print(
            "Undo:",
            transaction["type"],
            transaction["amount"]
        )

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

            self.history.append({
                "type": "withdraw",
                "amount": amount
            })

            self._notify(
                f"{self.owner} withdrew {amount}"
            )

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



class AccountRegistry:

    def __init__(self):

        self.accounts = {}
        self.order = []


    def add(self, account):

        self.accounts[account.number] = account
        self.order.append(account)


    def find(self, number):

        return self.accounts.get(number)


    def list_all(self):

        return self.order



sms = SMSAlert()
audit = AuditLog()


registry = AccountRegistry()


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
account1.subscribe(audit)

account2.subscribe(sms)
account2.subscribe(audit)


registry.add(account1)
registry.add(account2)


account1.deposit(500)

account1.withdraw(200)

account2.deposit(300)

account2.withdraw(700)



print("\nFind Account:")

found = registry.find("1001")

print(found.statement())


print("\nAll Accounts:")

for account in registry.list_all():

    print(account.statement())


print("\nTransaction History:")

print(account1.history)


print("\nUndo Last Transaction:")

account1.undo_last()

print(account1.statement())