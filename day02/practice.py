# Exercise 1
print("Exercise 1: Temperature Label")

temperature = float(input("Enter temperature in °C: "))

if temperature < 15:
    print("cold")
elif temperature <= 28:
    print("warm")
else:
    print("hot")

# Exercise 2
print("\nExercise 2: Receipt Loop")

for number in range(1, 11):
    print(f"Receipt #{number}")

# Exercise 3
print("\nExercise 3: Even Numbers")

for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# Exercise 4
print("\nExercise 4: Discount Function")

def apply_discount(price, percent=10):
    discount = price * (percent / 100)
    return price - discount

print(apply_discount(100))
print(apply_discount(100, 20))

# Exercise 5
print("\nExercise 5: Countdown")

count = 5

while count > 0:
    print(count)
    count -= 1

print("Liftoff!")