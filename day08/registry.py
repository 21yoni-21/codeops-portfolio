
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


def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1



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


# -----------------------------
# Account
# -----------------------------
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

    def statement(self):
        return f"{self.owner} ({self.number}) Balance = {self.balance}"



class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.rate = config.interest_rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)



class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.overdraft = config.overdraft_limit

    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            self.history.append(("withdraw", amount))
        else:
            print("Overdraft exceeded")


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
        self.by_number = {}
        self.order = []

    def add(self, acc):
        self.by_number[acc.number] = acc
        self.order.append(acc.number)

   
    def top_by_balance(self, n=5):

        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )

        return accounts[:n]

   
    def find_by_number(self, number):

        nums = sorted(self.by_number.keys())

        index = binary_search(nums, number)

        if index >= 0:
            return self.by_number[nums[index]]

        return None

 
    def total_transactions(self, number):

        account = self.find_by_number(number)

        if account is None:
            return 0

        amounts = []

        for action, amount in account.history:
            amounts.append(amount)

        return self.recursive_total(amounts)

    def recursive_total(self, nums):

        if len(nums) == 0:
            return 0

        return nums[0] + self.recursive_total(nums[1:])


    def list_all(self):

        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts


registry = AccountRegistry()

acc1 = SavingsAccount("Abel", 101, 5000)
acc2 = CurrentAccount("Sara", 102, 9000)
acc3 = SavingsAccount("John", 103, 3000)

acc1.deposit(1000)
acc1.withdraw(500)

acc2.deposit(500)

acc3.deposit(200)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

print("Top 2 Balances")
for account in registry.top_by_balance(2):
    print(account.statement())

print()

print("Find Account 102")
account = registry.find_by_number(102)

if account:
    print(account.statement())

print()

print("Total Transactions for Account 101")
print(registry.total_transactions(101))