import json
import os
from datetime import datetime

class FinanceTracker:
    def __init__(self, filename='finance_data.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("⚠️ Corrupted data file. Resetting to empty.")
        return {'income': [], 'expenses': []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_transaction(self, amount, category, t_type, note=""):
        entry = {
            'amount': round(amount, 2),
            'category': category,
            'note': note,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        if t_type == 'income':
            self.data['income'].append(entry)
            print(f"✅ Income of ₹{amount:.2f} added under '{category}'.")
        elif t_type == 'expense':
            self.data['expenses'].append(entry)
            print(f"✅ Expense of ₹{amount:.2f} recorded for '{category}'.")

        self.save_data()

    def view_summary(self):
        total_income = sum(item['amount'] for item in self.data['income'])
        total_expense = sum(item['amount'] for item in self.data['expenses'])
        balance = total_income - total_expense

        print("\n📊 Financial Summary")
        print("-" * 30)
        print(f"💰 Total Income : ₹{total_income:.2f}")
        print(f"💸 Total Expenses: ₹{total_expense:.2f}")
        print(f"🧮 Net Balance  : ₹{balance:.2f}")
        print("-" * 30)

    def list_transactions(self, t_type):
        entries = self.data.get(t_type, [])
        print(f"\n📂 {'Income' if t_type == 'income' else 'Expense'} Transactions:")
        if not entries:
            print("No entries yet.")
            return

        for idx, entry in enumerate(entries, 1):
            print(f"{idx}. ₹{entry['amount']:.2f} | {entry['category']} | {entry['note']} | {entry['timestamp']}")


def print_menu():
    print("\n========= Personal Finance Tracker =========")
    print("1. ➕ Add Income")
    print("2. ➖ Add Expense")
    print("3. 📈 View Summary")
    print("4. 📂 View All Income")
    print("5. 📂 View All Expenses")
    print("6. ❌ Exit")
    print("============================================")


def get_amount_input():
    while True:
        try:
            amt = float(input("Enter amount (₹): "))
            if amt <= 0:
                raise ValueError
            return amt
        except ValueError:
            print("❌ Invalid amount. Enter a positive number.")


def main():
    tracker = FinanceTracker()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            amt = get_amount_input()
            cat = input("Enter income source/category: ")
            note = input("Optional note: ")
            tracker.add_transaction(amt, cat, 'income', note)

        elif choice == '2':
            amt = get_amount_input()
            cat = input("Enter expense category: ")
            note = input("Optional note: ")
            tracker.add_transaction(amt, cat, 'expense', note)

        elif choice == '3':
            tracker.view_summary()

        elif choice == '4':
            tracker.list_transactions('income')

        elif choice == '5':
            tracker.list_transactions('expenses')

        elif choice == '6':
            print("👋 Thank you for using Personal Finance Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
