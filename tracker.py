import csv

# File to store expenses
FILENAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])

    print("Expense added successfully!\n")

def view_expenses():
    print("\nYour Expenses:")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Amount: {row[0]}, Category: {row[1]}, Date: {row[2]}")
    print()

# Main Menu
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
