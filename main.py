
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

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense['amount']:.2f} | {expense['category']} | {expense['description']}")

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            print(f"Deleted: ₹{deleted['amount']:.2f} | {deleted['description']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
def search_expenses():
        if not expenses:
            print("No expenses recorded.")
            return

        search_term = input("Enter category or description to search: ").lower()

        found = False

        print("\n--- Search Results ---")

        for expense in expenses:
            if (search_term in expense["category"].lower() or
                search_term in expense["description"].lower()):

                print(
                f"₹{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )

            found = True

        if not found:
            print("No matching expenses found.")
def show_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0
    category_totals = {}

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        total += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n===== SUMMARY =====")
    print(f"Total Spending: ₹{total:.2f}")

    print("\n--- Category-wise Spending ---")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expenses")
    print("5. Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        search_expenses()
    elif choice == "5":
        show_summary()
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")