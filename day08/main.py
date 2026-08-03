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

        self.history.append(
            ("deposit", amount)
        )

        self._notify(
            f"{self.owner} deposited {amount}"
        )



    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            self.history.append(
                ("withdraw", amount)
            )

            self._notify(
                f"{self.owner} withdrew {amount}"
            )

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

        return (
            f"Account: {self.owner} "
            f"Balance = {self.balance}"
        )



class SavingsAccount(Account):


    def __init__(self, owner, number, balance=0):

        super().__init__(
            owner,
            number,
            balance
        )

        self.rate = config.interest_rate



    def add_interest(self):

        interest = self.balance * self.rate

        self.deposit(interest)



    def statement(self):

        return (
            f"Savings Account: "
            f"{self.owner} "
            f"Balance = {self.balance}"
        )



class CurrentAccount(Account):


    def __init__(self, owner, number, balance=0):

        super().__init__(
            owner,
            number,
            balance
        )

        self.overdraft = config.overdraft_limit



    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft:

            self.balance -= amount

            self.history.append(
                ("withdraw", amount)
            )

            self._notify(
                f"{self.owner} withdrew {amount}"
            )

        else:

            print("Overdraft exceeded")



    def statement(self):

        return (
            f"Current Account: "
            f"{self.owner} "
            f"Balance = {self.balance}"
        )



class AccountFactory:


    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":

            return SavingsAccount(
                owner,
                number,
                balance
            )


        elif kind == "current":

            return CurrentAccount(
                owner,
                number,
                balance
            )


        else:

            raise ValueError(
                "Unknown account type"
            )



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

            accounts.append(
                self.by_number[number]
            )

        return accounts



    # Day 08 - Leaderboard

    def top_by_balance(self, n):

        return sorted(
            self.list_all(),
            key=lambda acc: acc.balance,
            reverse=True
        )[:n]



    # Day 08 - Binary Search O(log n)

    def find_by_number(self, number):

        accounts = sorted(
            self.list_all(),
            key=lambda acc: acc.number
        )


        left = 0
        right = len(accounts) - 1


        while left <= right:


            middle = (left + right) // 2


            if accounts[middle].number == number:

                return accounts[middle]


            elif accounts[middle].number < number:

                left = middle + 1


            else:

                right = middle - 1


        return None



    # Day 08 - Recursive total

    def total_transactions_recursive(
        self,
        history,
        index=0
    ):


        if index == len(history):

            return 0


        return (
            1 +
            self.total_transactions_recursive(
                history,
                index + 1
            )
        )



    def total_transactions(self, number):

        account = self.find(number)


        if account is None:

            return 0


        return self.total_transactions_recursive(
            account.history
        )



sms = SMSAlert()


registry = AccountRegistry()


acc1 = AccountFactory.create(
    "savings",
    "Yonas",
    "1001",
    3000
)


acc2 = AccountFactory.create(
    "current",
    "Abel",
    "1002",
    1500
)


acc3 = AccountFactory.create(
    "savings",
    "Sara",
    "1003",
    5000
)


acc1.subscribe(sms)
acc2.subscribe(sms)
acc3.subscribe(sms)


registry.add(acc1)
registry.add(acc2)
registry.add(acc3)


acc1.deposit(500)
acc1.withdraw(200)

acc2.deposit(100)

acc3.deposit(1000)



print("\nTop Accounts:")

for acc in registry.top_by_balance(2):

    print(acc.statement())



print("\nBinary Search:")

result = registry.find_by_number("1002")

print(result.statement())



print("\nTotal Transactions:")

print(
    registry.total_transactions("1001")
)