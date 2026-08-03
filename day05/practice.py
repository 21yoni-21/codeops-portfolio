#exercise .......py.............................
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


car1 = Car("Toyota", "Corolla")
truck1 = Truck("Volvo", "FH16")

print(car1.describe())
print(truck1.describe())


#exercise 2 ...............................

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"Make: {self.make}, Model: {self.model}")


class Truck(Vehicle):

    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity


truck = Truck("Isuzu", "NPR", "5 Tons")

truck.describe()
print("Capacity:", truck.capacity)


#exercise ..........................................

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"Make: {self.make}, Model: {self.model}")


class Truck(Vehicle):

    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        print(f"Make: {self.make}, Model: {self.model}, Capacity: {self.capacity}")


truck = Truck("Volvo", "FH16", "10 Tons")

truck.describe()

#exercise......................................

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")


class Car(Vehicle):
    pass


class Truck(Vehicle):

    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        print(f"{self.make} {self.model} - Capacity: {self.capacity}")


vehicles = [
    Car("Toyota", "Corolla"),
    Car("Honda", "Civic"),
    Truck("Volvo", "FH16", "10 Tons")
]

for vehicle in vehicles:
    vehicle.describe()

    #exercise .........................

    from abc import ABC, abstractmethod


# Abstract Class
class Vehicle(ABC):

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def wheels(self):
        pass


# Car Clas
class Car(Vehicle):

    def wheels(self):
        return 4


# Truck Class
class Truck(Vehicle):

    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def wheels(self):
        return 6


# Test
car = Car("Toyota", "Corolla")
truck = Truck("Volvo", "FH16", "10 Tons")

print(car.wheels())
print(truck.wheels())


#added..............................................
from account import Account
from accounts import SavingsAccount, CurrentAccount


# Create accounts

account1 = Account("Yonas", "001", 500)

savings = SavingsAccount(
    "Abel",
    "002",
    1000,
    0.05
)

current = CurrentAccount(
    "Marta",
    "003",
    200,
    500
)


# Add interest to savings account

savings.add_interest()


# Withdraw from current account

current.withdraw(600)


# Polymorphism loop

accounts = [
    account1,
    savings,
    current
]


for account in accounts:
    print(account.statement())