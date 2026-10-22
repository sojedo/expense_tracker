
import json
CURRENCY = "\u20a6" 
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
except json.JSONDecodeError:
    raise SystemExit("expenses.json is damaged/empty. Fix or delete it, then restart.")

while True:
    print("\n=== CLI Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("q. Quit")

    choice = input("choose 1-q: ").lower().strip()

    if choice == "1":
        description = input("Enter description: ").strip()
        if not description:
            print("cannot be empty")
            continue
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("invalid input")
            continue
        if amount <= 0:
            print("enter positive number")
            continue
        expense = {"description": description, "amount": amount}
        expenses.append(expense)
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        print("Expense added")

    elif choice == "q":
        
        break

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for number, expense in enumerate(expenses, start=1):
                print(f"{number}. {expense['description']} - ₦{expense['amount']:.2f}")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense['amount']
        print(f"Total spent: ₦{total:.2f}")

    else:
         print("invalid input: try 1, 2, 3, q")
        