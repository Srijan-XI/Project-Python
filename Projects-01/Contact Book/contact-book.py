import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

    def view_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                return True
        return False

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

class ContactApp:
    def __init__(self, root):
        self.manager = ContactManager()
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f0f0")

        self.list_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.list_frame.pack(pady=10)

        self.listbox = Listbox(self.list_frame, width=50, height=10, font=("Arial", 12), bg="#ffffff", selectmode=tk.SINGLE)
        self.listbox.grid(row=0, column=0)

        scrollbar = Scrollbar(self.list_frame)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, width=15, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.grid(row=0, column=0, padx=10)

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts, width=15, height=2, bg="#2196F3", fg="white", font=("Arial", 12))
        self.view_button.grid(row=0, column=1, padx=10)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, width=15, height=2, bg="#FFC107", fg="white", font=("Arial", 12))
        self.search_button.grid(row=0, column=2, padx=10)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, width=15, height=2, bg="#FF5722", fg="white", font=("Arial", 12))
        self.update_button.grid(row=1, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, width=15, height=2, bg="#F44336", fg="white", font=("Arial", 12))
        self.delete_button.grid(row=1, column=1, padx=10, pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        if name and phone:
            self.manager.add_contact(name, phone, email, address)
            messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
            self.view_contacts()

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.manager.view_contacts():
            self.listbox.insert(tk.END, contact)

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        if search_term:
            results = self.manager.search_contact(search_term)
            self.listbox.delete(0, tk.END)
            if results:
                for contact in results:
                    self.listbox.insert(tk.END, contact)
            else:
                messagebox.showinfo("Search Result", "No contacts found.")

    def update_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            contact = self.manager.view_contacts()[selected_contact[0]]
            name = contact.name
            new_phone = simpledialog.askstring("Input", "Enter new phone number (leave blank to keep current):")
            new_email = simpledialog.askstring("Input", "Enter new email (leave blank to keep current):")
            new_address = simpledialog.askstring("Input", "Enter new address (leave blank to keep current):")
            updated = self.manager.update_contact(name, new_phone if new_phone else None, new_email if new_email else None, new_address if new_address else None)
            if updated:
                messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
                self.view_contacts()
            else:
                messagebox.showerror("Error", f"Contact '{name}' not found.")

    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            contact = self.manager.view_contacts()[selected_contact[0]]
            name = contact.name
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the contact '{name}'?")
            if confirm:
                deleted = self.manager.delete_contact(name)
                if deleted:
                    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
                    self.view_contacts()
                else:
                    messagebox.showerror("Error", f"Contact '{name}' not found.")
        else:
            messagebox.showwarning("Selection Error", "Select a contact to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
