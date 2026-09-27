
expenses = []

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")

    for expense in expenses:
        print(f"₹{expense['amount']:.2f} | {expense['category']} | {expense['description']}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")