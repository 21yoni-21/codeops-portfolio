#Exercise 1........................
cities = [
    "Addis Ababa",
    "Adama",
    "Hawassa",
    "Addis Ababa",
    "Bahir Dar",
    "Hawassa",
    "Mekelle"
]

unique_cities = set(cities)

print("Distinct cities:")
for city in unique_cities:
    print(city)

print("Count:", len(unique_cities))


#Exerciese 2...............................
# Dictionary of grocery items and prices (ETB)

prices = {
    "Bread": 50,
    "Milk": 80,
    "Eggs": 120,
    "Sugar": 90,
    "Rice": 150
}

# Print each item and price
for item, price in prices.items():
    print(f"{item}: {price} ETB")


#Exerciese 3 ........................................

prices = [100, 250, 400, 80]

with_tax = [price * 1.15 for price in prices]

print(with_tax)

#Exercise 4.................................................
prices = [100, 250, 400, 80]

cheap_items = [price for price in prices if price < 200]

print(cheap_items)

#Exercise 5.............................


# Write names to the file
with open("names.txt", "w") as file:
    file.write("Abel\n")
    file.write("Sara\n")
    file.write("Yonas\n")

# Read the file
with open("names.txt") as file:
    for line in file:
        print(line.strip())

#Exercise 6..............................

try:
    number = int(input("Enter a number: "))
    result = 1000 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Done")