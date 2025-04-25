import os
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        """Loads contacts from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    name = lines[i].strip()
                    phone = lines[i + 1].strip()
                    email = lines[i + 2].strip()
                    self.contacts.append(Contact(name, phone, email))

    def save_contacts(self):
        """Saves contacts to the file."""
        with open(self.filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name}\n{contact.phone}\n{contact.email}\n")

    def add_contact(self, name, phone, email):
        """Adds a new contact."""
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
        return "Contact added successfully!"

    def search_contact(self, name):
        """Searches for a contact by name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}"
        return "Contact not found."

    def delete_contact(self, name):
        """Deletes a contact by name."""
        original_length = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        if len(self.contacts) < original_length:
            self.save_contacts()
            return "Contact deleted successfully!"
        return "Contact not found."

# GUI Application
class AddressBookGUI:
    def __init__(self, root):
        self.address_book = AddressBook()
        self.root = root
        self.root.title("Address Book")

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Search Contact", command=self.search_contact).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).grid(row=0, column=3, padx=10, pady=10)
        tk.Button(root, text="Exit", command=root.quit).grid(row=0, column=4, padx=10, pady=10)

        # Listbox to show contacts
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

    def add_contact(self):
        """Gets input from the user and adds a contact."""
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone:")
        email = simpledialog.askstring("Input", "Enter Email:")
        if name and phone and email:
            messagebox.showinfo("Success", self.address_book.add_contact(name, phone, email))
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def view_contacts(self):
        """Displays all contacts in the Listbox."""
        self.listbox.delete(0, tk.END)
        if not self.address_book.contacts:
            self.listbox.insert(tk.END, "No contacts found.")
        else:
            for contact in self.address_book.contacts:
                self.listbox.insert(tk.END, f"{contact.name} - {contact.phone} - {contact.email}")

    def search_contact(self):
        """Searches for a contact and displays the result."""
        name = simpledialog.askstring("Search", "Enter name to search:")
        if name:
            result = self.address_book.search_contact(name)
            messagebox.showinfo("Search Result", result)

    def delete_contact(self):
        """Deletes a contact and refreshes the list."""
        name = simpledialog.askstring("Delete", "Enter name to delete:")
        if name:
            result = self.address_book.delete_contact(name)
            messagebox.showinfo("Delete Contact", result)
            self.view_contacts()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = AddressBookGUI(root)
    root.mainloop()
