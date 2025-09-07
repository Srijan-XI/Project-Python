<<<<<<< HEAD
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    name = lines[i].strip()
                    phone = lines[i + 1].strip()
                    email = lines[i + 2].strip()
                    self.contacts.append(Contact(name, phone, email))

    def save_contacts(self):
        with open(self.filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name}\n{contact.phone}\n{contact.email}\n")

    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContacts:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self):
        name = input("Enter the name to search: ").strip()
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Found Contact - Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ").strip()
        original_length = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        
        if len(self.contacts) < original_length:
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def print_menu():
    print("\nAddress Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    address_book = AddressBook()
    
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            address_book.add_contact()
        elif choice == "2":
            address_book.view_contacts()
        elif choice == "3":
            address_book.search_contact()
        elif choice == "4":
            address_book.delete_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
=======
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    name = lines[i].strip()
                    phone = lines[i + 1].strip()
                    email = lines[i + 2].strip()
                    self.contacts.append(Contact(name, phone, email))

    def save_contacts(self):
        with open(self.filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name}\n{contact.phone}\n{contact.email}\n")

    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContacts:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self):
        name = input("Enter the name to search: ").strip()
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Found Contact - Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ").strip()
        original_length = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        
        if len(self.contacts) < original_length:
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def print_menu():
    print("\nAddress Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    address_book = AddressBook()
    
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            address_book.add_contact()
        elif choice == "2":
            address_book.view_contacts()
        elif choice == "3":
            address_book.search_contact()
        elif choice == "4":
            address_book.delete_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
