Expense Tracker

A Python-based personal expense management application that helps users record, manage, and analyze their spending.

Features
Add expenses
Automatically record expense dates
View all expenses
Update existing expenses
Delete expenses
Search expenses by category or description
Calculate total spending
View category-wise spending
Generate monthly spending summaries
Set a monthly budget
Check monthly budget status
Detect budget overruns
Save expenses using CSV
Load expenses automatically when the application starts
Save monthly budget between sessions
Technologies Used
Python
CSV
Git
GitHub
Project Structure

expense-tracker
│
├── main.py
├── README.md
└── .gitignore

expenses.csv and budget.txt are local data files and are excluded from Git tracking.

How to Run
Clone the repository.
Open the project folder in VS Code.
Run:
python main.py
Application Menu

1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expenses
5. Update Expense
6. Summary
7. Monthly Summary
8. Set Monthly Budget
9. Check Budget
10. Exit
    Data Persistence

Expense information is stored locally in a CSV file.

The monthly budget is stored separately so that it remains available after restarting the application.

Future Improvements-
*Graphical user interface
*Database integration
*Expense charts and visual analytics
*Category-based budget limits

Screenshots:
1.Main Menu

2.Expenses and Monthly Summary

3.Budget Status
