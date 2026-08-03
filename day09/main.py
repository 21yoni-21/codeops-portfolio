from collections import deque


class Branch:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.children = []


    def add_child(self, branch):
        self.children.append(branch)



def total_balance(branch):

    total = branch.balance

    for child in branch.children:
        total += total_balance(child)

    return total



class TransferGraph:

    def __init__(self):

        self.graph = {}


    def add_branch(self, branch):

        if branch not in self.graph:
            self.graph[branch] = []


    def add_transfer(self, from_branch, to_branch):

        if from_branch not in self.graph:
            self.graph[from_branch] = []

        self.graph[from_branch].append(to_branch)



    def bfs(self, start):

        visited = []

        queue = deque([start])


        while queue:

            current = queue.popleft()


            if current not in visited:

                visited.append(current)


                for neighbor in self.graph.get(current, []):

                    queue.append(neighbor)


        return visited




# -----------------------------
# Branch Tree
# -----------------------------


head_office = Branch(
    "Head Office",
    100000
)


addis_region = Branch(
    "Addis Region",
    50000
)


mekelle_region = Branch(
    "Mekelle Region",
    40000
)


cbe1 = Branch(
    "CBE-1",
    20000
)


cbe2 = Branch(
    "CBE-2",
    15000
)


cbe3 = Branch(
    "CBE-3",
    10000
)


cbe4 = Branch(
    "CBE-4",
    12000
)



head_office.add_child(addis_region)

head_office.add_child(mekelle_region)


addis_region.add_child(cbe1)

addis_region.add_child(cbe2)


mekelle_region.add_child(cbe3)

mekelle_region.add_child(cbe4)



# -----------------------------
# Recursive Branch Total
# -----------------------------


print("Total Bank Balance:")

print(
    total_balance(head_office)
)



# -----------------------------
# Transfer Graph
# -----------------------------


bank_graph = TransferGraph()



bank_graph.add_transfer(
    "CBE-1",
    "CBE-2"
)


bank_graph.add_transfer(
    "CBE-1",
    "CBE-3"
)


bank_graph.add_transfer(
    "CBE-2",
    "CBE-4"
)


bank_graph.add_transfer(
    "CBE-3",
    "CBE-4"
)



# -----------------------------
# BFS Traversal
# -----------------------------


print("\nBranches reachable from CBE-1:")


reachable = bank_graph.bfs("CBE-1")


for branch in reachable:

    print(branch)