

numbers = [10, 20, 30, 40, 50]
print(numbers[3])

for num in numbers:
    print(num)



for i in numbers:
    for j in numbers:
        pass

print("Nested loop completed")


accounts = {
    "1001": "Yonas",
    "1002": "Abel"
}

print(accounts["1002"])


def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


sorted_numbers = list(range(1, 101))

print(binary_search(sorted_numbers, 75))


print("\n==========================")

#exercise 2 


import time

account_list = []
account_dict = {}

for i in range(100000):
    account = f"ACC{i}"
    account_list.append(account)
    account_dict[account] = i

target = "ACC99999"

start = time.perf_counter()
found = target in account_list
end = time.perf_counter()

print("List lookup:", end - start)

start = time.perf_counter()
found = target in account_dict
end = time.perf_counter()

print("Dict lookup:", end - start)

#exercise  3 ........................................

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()

names = ["Yonas", "Abel", "Marta", "Helen"]

for name in names:
    stack.push(name)

reversed_names = []

while stack.items:
    reversed_names.append(stack.pop())

print(reversed_names)

#exercise

from collections import deque

queue = deque()

queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")
queue.append("Customer 4")
queue.append("Customer 5")

while queue:
    print(queue.popleft())

#exercise...............................

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


linked = LinkedList()

linked.push_front("Abel")
linked.push_front("Helen")
linked.push_front("Yonas")

linked.print_all()

#added
from registry import Account, AccountRegistry


registry = AccountRegistry()


acc1 = Account(
    "Yonas",
    "001",
    1000
)

acc2 = Account(
    "Abel",
    "002",
    500
)


registry.add(acc1)
registry.add(acc2)


acc1.deposit(500)

acc1.withdraw(200)


print("Balance before undo:", acc1.balance)


acc1.undo_last()


print("Balance after undo:", acc1.balance)


found = registry.find("001")

print("Found account:", found.owner)


print("All accounts:")

for account in registry.list_all():
    print(account.owner, account.balance)
