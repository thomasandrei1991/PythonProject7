print("Expense Tracker")
print("1. Add Expense")
print("2. View total & list")
print("3. Exit")
descriptions = []
amounts = []
while True:
    choice = input("\nChoose: ")
    if choice == "1":
        description = input("Description: ")
        amount = int(input("Amount: "))
        descriptions.append(description)
        amounts.append(amount)
        print("Added!")
    elif choice == "2":
        print("Expenses:")
        Total = 0
        for description, amount in zip(descriptions, amounts):
            print(f"\u2022 {description:10} {amount:4}")
            Total += amount
        print("-----------------------")
        print(f"Total: {Total:10}")
    elif choice == "3":
        print("Thankyou!")
        break










#total and subtotal