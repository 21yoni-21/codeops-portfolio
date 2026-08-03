stock = {}

try:
    with open("stock.txt") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file yet - starting empty")


def adjust(item, amount):
   stock[item] = stock.get(item, 0) + amount


adjust("Bandage", 5)
adjust("Amoxicillin", -3)

low = [item for item, qty in stock.items() if qty < 10]

print("Low stock:", low)

with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")