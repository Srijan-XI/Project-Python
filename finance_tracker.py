import json
import os

class FinanceTracker:
    def __init__(self, filename='finance_data.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {'income': [], 'expenses': []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add_income(self, amount, source):
        self.data['income'].append({'amount': amount, 'source': source})
        self.save_data()
        print(f"Added income: ${amount} from {source}")

    def add_expense(self, amount, category):
        self.data['expenses'].append({'amount': amount, 'category': category})
        self.save_data()
        print(f"Added expense: ${amount} for {category}")

    def view_summary(self):
        total_income = sum(item['amount'] for item in self.data['income'])
        total_expenses = sum(item['amount'] for item in self.data['expenses'])
        balance = total_income - total_expenses

        print("\nFinancial Summary:")
        print(f"Total Income: ${total_income}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Balance: ${balance}")

def print_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

def main():
    tracker = FinanceTracker()

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            tracker.add_income(amount, source)

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)

        elif choice == '3':
            tracker.view_summary()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
