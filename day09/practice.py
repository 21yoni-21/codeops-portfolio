#exercise  .....................1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def in_order(node):
    if node is None:
        return

    in_order(node.left)
    print(node.value)
    in_order(node.right)


balances = [5000, 2000, 8000, 1000, 3000, 7000, 9000]

root = None

for balance in balances:
    root = insert(root, balance)

print("BST sorted balances:")

in_order(root)

#exercise 2......................................

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


root = Node(10)

root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(7)


print("Tree height:")
print(height(root))

#exercise 3..................................


from collections import deque


graph = {
    "Almaz": ["Dawit", "Tigist", "Samuel"],
    "Dawit": ["Almaz", "Hanna"],
    "Tigist": ["Almaz", "Samuel"],
    "Samuel": ["Almaz", "Tigist", "Hanna"],
    "Hanna": ["Dawit", "Samuel"]
}


def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


result = bfs(graph, "Almaz")

print("BFS reachable vertices:")
print(result)


#exercise 4.............................................

graph = {
    "Almaz": ["Dawit", "Tigist", "Samuel"],
    "Dawit": ["Almaz", "Hanna"],
    "Tigist": ["Almaz", "Samuel"],
    "Samuel": ["Almaz", "Tigist", "Hanna"],
    "Hanna": ["Dawit", "Samuel"]
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print("DFS visit order:")
print(dfs(graph, "Almaz"))

#exercise 5....................................

import heapq


tasks = []


heapq.heappush(tasks, (3, "Pay electricity bill"))
heapq.heappush(tasks, (1, "Emergency meeting"))
heapq.heappush(tasks, (5, "Buy groceries"))
heapq.heappush(tasks, (2, "Finish assignment"))
heapq.heappush(tasks, (4, "Call customer"))


print("Tasks by priority:")


while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, "-", task)