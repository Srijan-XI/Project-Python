import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import json
import os
from cryptography.fernet import Fernet
import base64
import hashlib

# Generate a secure key from a master password
def generate_key(master_password):
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Password Generator
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Password Manager Class
class PasswordManager:
    def __init__(self, master_password, filename="passwords.json"):
        self.filename = filename
        self.key = generate_key(master_password)
        self.cipher = Fernet(self.key)
        self.passwords = self.load_passwords()

    def load_passwords(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    encrypted_data = file.read().encode()
                    decrypted_data = self.cipher.decrypt(encrypted_data)
                    return json.loads(decrypted_data)
                except:
                    messagebox.showerror("Error", "Incorrect master password or corrupted file.")
                    return {}
        return {}

    def save_passwords(self):
        encrypted_data = self.cipher.encrypt(json.dumps(self.passwords).encode())
        with open(self.filename, "w") as file:
            file.write(encrypted_data.decode())

    def add_password(self, site, username, password):
        self.passwords[site] = {"username": username, "password": password}
        self.save_passwords()
        messagebox.showinfo("Success", f"Password for {site} saved securely!")

    def get_password(self, site):
        return self.passwords.get(site, None)

    def delete_password(self, site):
        if site in self.passwords:
            del self.passwords[site]
            self.save_passwords()
            messagebox.showinfo("Success", f"Password for {site} deleted securely!")
        else:
            messagebox.showerror("Error", "No password found for this site.")

# GUI Class
class PasswordManagerGUI:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("🔐 Secure Password Manager")
        self.root.geometry("400x500")

        # Title Label
        tk.Label(root, text="🔐 Secure Password Manager", font=("Arial", 14, "bold")).pack(pady=10)

        # Site Entry
        self.site_label = tk.Label(root, text="Website:")
        self.site_label.pack()
        self.site_entry = tk.Entry(root, width=40)
        self.site_entry.pack(pady=5)

        # Username Entry
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root, width=40)
        self.username_entry.pack(pady=5)

        # Password Entry
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, width=40, show="*")
        self.password_entry.pack(pady=5)

        # Generate Password Button
        self.generate_button = tk.Button(root, text="🔄 Generate Password", command=self.generate_new_password)
        self.generate_button.pack(pady=5)

        # Save Password Button
        self.save_button = tk.Button(root, text="💾 Save Password", command=self.save_password)
        self.save_button.pack(pady=5)

        # Retrieve Password Button
        self.retrieve_button = tk.Button(root, text="🔍 Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack(pady=5)

        # View All Button
        self.view_all_button = tk.Button(root, text="📜 View All", command=self.view_all_passwords)
        self.view_all_button.pack(pady=5)

        # Delete Password Button
        self.delete_button = tk.Button(root, text="🗑 Delete Password", command=self.delete_password)
        self.delete_button.pack(pady=5)

    def generate_new_password(self):
        password = generate_password(16)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if site and username and password:
            self.manager.add_password(site, username, password)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill all fields!")

    def retrieve_password(self):
        site = self.site_entry.get()
        if site:
            result = self.manager.get_password(site)
            if result:
                messagebox.showinfo("Retrieved Password", f"📌 Site: {site}\n👤 Username: {result['username']}\n🔑 Password: {result['password']}")
            else:
                messagebox.showerror("Error", "No password found for this site.")
        else:
            messagebox.showerror("Error", "Please enter a site name!")

    def view_all_passwords(self):
        passwords = self.manager.passwords
        if passwords:
            all_data = "\n".join([f"📌 {site}: {data['username']} | {data['password']}" for site, data in passwords.items()])
            messagebox.showinfo("Saved Passwords", all_data)
        else:
            messagebox.showinfo("Info", "No passwords saved yet!")

    def delete_password(self):
        site = self.site_entry.get()
        if site:
            self.manager.delete_password(site)
        else:
            messagebox.showerror("Error", "Please enter a site name!")

    def clear_entries(self):
        self.site_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Run the GUI
if __name__ == "__main__":
    master_password = simpledialog.askstring("🔑 Master Password", "Enter your master password:", show="*")
    if master_password:
        manager = PasswordManager(master_password)
        root = tk.Tk()
        app = PasswordManagerGUI(root, manager)
        root.mainloop()
    else:
        messagebox.showerror("Error", "Master password is required!")
