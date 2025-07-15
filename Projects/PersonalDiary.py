import json
import os
from datetime import datetime

class Diary:
    def __init__(self, filename='diary_entries.json'):
        self.filename = filename
        self.entries = self.load_entries()

    def load_entries(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_entries(self):
        with open(self.filename, 'w') as file:
            json.dump(self.entries, file)

    def add_entry(self):
        date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        content = input("Write your diary entry: ")
        entry = {'date': date, 'content': content}
        self.entries.append(entry)
        self.save_entries()
        print("Diary entry added successfully!")

    def view_entries(self):
        if not self.entries:
            print("No diary entries found.")
            return
        
        print("\nDiary Entries:")
        for entry in self.entries:
            print(f"Date: {entry['date']}\nContent: {entry['content']}\n")

    def search_entries(self):
        search_date = input("Enter the date to search (YYYY-MM-DD): ")
        found_entries = [entry for entry in self.entries if entry['date'] == search_date]

        if found_entries:
            print(f"\nDiary Entries for {search_date}:")
            for entry in found_entries:
                print(f"Content: {entry['content']}\n")
        else:
            print("No entries found for this date.")

def print_menu():
    print("\nPersonal Diary Menu")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries by Date")
    print("4. Exit")

def main():
    diary = Diary()

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            diary.add_entry()
        elif choice == '2':
            diary.view_entries()
        elif choice == '3':
            diary.search_entries()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
