import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

DATA_FILE = 'expenses.csv'

def add_expense():
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    category = input("Enter category: ")
    description = input("Enter description: ")
    with open(DATA_FILE, 'a') as f:
        f.write(f"{date_str},{amount},{category},{description}\n")
    print("Expense added successfully!\n")

def load_data():
    if not os.path.exists(DATA_FILE):
        print("No expenses found. Please add some expenses first.\n")
        return None
    df = pd.read_csv(DATA_FILE, names=['Date', 'Amount', 'Category', 'Description'], parse_dates=['Date'])
    return df

def plot_monthly_trends(df):
    df['Month'] = df['Date'].dt.to_period('M')
    monthly = df.groupby('Month')['Amount'].sum()
    monthly.plot(kind='line', marker='o')
    plt.title('Monthly Spending Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Spent')
    plt.tight_layout()
    plt.show()

def plot_category_pie(df):
    category_totals = df.groupby('Category')['Amount'].sum()
    category_totals.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Spending by Category')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

def plot_category_bar(df):
    category_totals = df.groupby('Category')['Amount'].sum()
    category_totals.plot(kind='bar', color='skyblue')
    plt.title('Expense Comparison by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Spent')
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nExpense Tracker and Analyzer")
        print("1. Add Expense")
        print("2. Show Monthly Spending Trends")
        print("3. Show Pie Chart by Category")
        print("4. Show Bar Chart by Category")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice in {'2', '3', '4'}:
            df = load_data()
            if df is None:
                continue
            if choice == '2':
                plot_monthly_trends(df)
            elif choice == '3':
                plot_category_pie(df)
            elif choice == '4':
                plot_category_bar(df)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
