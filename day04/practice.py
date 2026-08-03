#Exercise 1....................................
class Book:
    # Constructor
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method
    def describe(self):
        print(f"{self.title} by {self.author} has {self.pages} pages.")


# Create two Book objects
book1 = Book("Python Basics", "John Smith", 250)
book2 = Book("Learn Git", "Sara Ali", 180)

# Call the method
book1.describe()
book2.describe()

#Exercise 2....................................

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n


product = Product("Milk", 80, 20)

print("Before:", product.quantity)

product.restock(10)

print("After restock:", product.quantity)

product.sell(5)

print("After selling:", product.quantity)

#Exercise 3 ....................................

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity


product = Product("Bread", 50, 15)

print(product.quantity)

#Exercise 4 ............................

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def sell(self, n):
        if n <= self.__quantity:
            self.__quantity -= n
        else:
            print("Not enough stock.")


product = Product("Milk", 80, 10)

product.sell(5)
print(product.quantity)

product.sell(20)
print(product.quantity)

#Exercise 5 ..............................................

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n


product1 = Product("Milk", 80, 20)
product2 = Product("Bread", 50, 30)
product3 = Product("Eggs", 120, 40)

product1.restock(10)

print(product1.name, product1.quantity)
print(product2.name, product2.quantity)
print(product3.name, product3.quantity)
