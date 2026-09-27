import csv
from datetime import datetime
expenses = []
def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date","amount", "category", "description"]
        )

        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

    except FileNotFoundError:
        pass

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%d-%m-%Y")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")

    for expense in expenses:
        print(f"{expense['date']} | "
    f"₹{expense['amount']:.2f} | "
    f"{expense['category']} | "
    f"{expense['description']}")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"{expense['date']} | "
    f"₹{expense['amount']:.2f} | "
    f"{expense['category']} | "
    f"{expense['description']}")

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            save_expenses()
            print(f"Deleted: ₹{deleted['amount']:.2f} | {deleted['description']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
def update_expense():
    if not expenses:
        print("No expenses to update.")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )

    try:
        choice = int(input("Enter expense number to update: "))

        if 1 <= choice <= len(expenses):
            expense = expenses[choice - 1]

            print("\nEnter new details:")

            expense["amount"] = float(input("Enter new amount: ₹"))
            expense["category"] = input("Enter new category: ")
            expense["description"] = input("Enter new description: ")

            save_expenses()

            print("Expense updated successfully!")

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
                f"{expense['date']} | "
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
load_expenses()
def show_monthly_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0
    category_totals = {}

    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%d-%m-%Y")

        if expense_date.month == int(month) and expense_date.year == int(year):
            amount = expense["amount"]
            category = expense["category"]

            total += amount

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print(f"\n===== SUMMARY FOR {month}-{year} =====")
    print(f"Total Spending: ₹{total:.2f}")

    if not category_totals:
        print("No expenses found for this month.")
        return

    print("\n--- Category-wise Spending ---")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expenses")
    print("5. Update Expense")
    print("6. Summary")
    print("7. Monthly Summary")
    print("8. Exit")

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
        update_expense()
    elif choice == "6":
        show_summary()
    elif choice == "7":
        show_monthly_summary()
    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")