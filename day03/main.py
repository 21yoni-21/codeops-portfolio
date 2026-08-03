customers = {}

try:
    with open("transactions.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            name, amount = line.split(",")
            amount = float(amount)

            if name in customers:
                customers[name] += amount
            else:
                customers[name] = amount

    sorted_customers = sorted(
        customers.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("Customer Spending Report")
    print("-" * 30)

    with open("report.txt", "w") as report:
        report.write("Customer Spending Report\n")
        report.write("-" * 30 + "\n")

        for name, total in sorted_customers:
            line = f"{name}: ETB {total:.2f}"
            print(line)
            report.write(line + "\n")

    print("\nReport saved to report.txt")

except FileNotFoundError:
    print("Error: transactions.txt was not found.")