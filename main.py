
import json

FILENAME = "expenses.json"

def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise SystemExit(f"{filename} is damaged/empty. Fix it, then restart.")

def save_expenses(expenses, filename):
    with open(filename, "w") as file:
        json.dump(expenses, file)

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total
def main():
    expenses = load_expenses(FILENAME)
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
            save_expenses(expenses, FILENAME)
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
            total = total_expenses(expenses)
            print(f"Total spent: ₦{total:.2f}")

        else:
            print("invalid input: try 1, 2, 3, q")

if __name__ == "__main__":
    main()
        