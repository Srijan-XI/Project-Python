import tkinter as tk
from tkinter import messagebox, simpledialog
import ttkbootstrap as ttk  # Modern themed GUI
import random
import string
import json
import os
from cryptography.fernet import Fernet
import base64
import hashlib

# File to store theme preference
THEME_FILE = "theme_pref.json"

# Generate a secure key from a master password
def generate_key(master_password):
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Password Generator
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

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
        messagebox.showinfo("Success", f"✅ Password for {site} saved securely!")

    def get_password(self, site):
        return self.passwords.get(site, None)

    def delete_password(self, site):
        if site in self.passwords:
            del self.passwords[site]
            self.save_passwords()
            messagebox.showinfo("Success", f"🗑️ Password for {site} deleted securely!")
        else:
            messagebox.showerror("Error", "No password found for this site.")

# GUI Class
class PasswordManagerGUI:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("🔐 Secure Password Manager")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Load saved theme preference
        self.current_theme = self.load_theme()

        # Frame for UI elements
        frame = ttk.Frame(root, padding=10)
        frame.pack(expand=True, fill="both")

        # Title Label
        ttk.Label(frame, text="🔐 Secure Password Manager", font=("Arial", 16, "bold"), bootstyle="primary").pack(pady=10)

        # Theme Toggle Button
        self.theme_button = ttk.Button(frame, text="🌗 Toggle Theme", bootstyle="secondary", command=self.toggle_theme)
        self.theme_button.pack(pady=5)

        # Site Entry
        ttk.Label(frame, text="🌐 Website:", font=("Arial", 12)).pack(anchor="w")
        self.site_entry = ttk.Entry(frame, width=40)
        self.site_entry.pack(pady=5)

        # Username Entry
        ttk.Label(frame, text="👤 Username:", font=("Arial", 12)).pack(anchor="w")
        self.username_entry = ttk.Entry(frame, width=40)
        self.username_entry.pack(pady=5)

        # Password Entry
        ttk.Label(frame, text="🔑 Password:", font=("Arial", 12)).pack(anchor="w")
        self.password_entry = ttk.Entry(frame, width=40, show="*")
        self.password_entry.pack(pady=5)

        # Buttons (Enhanced Styling)
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=10)

        self.generate_button = ttk.Button(button_frame, text="🔄 Generate", bootstyle="success", command=self.generate_new_password)
        self.generate_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(button_frame, text="💾 Save", bootstyle="primary", command=self.save_password)
        self.save_button.grid(row=0, column=1, padx=5)

        self.retrieve_button = ttk.Button(button_frame, text="🔍 Retrieve", bootstyle="warning", command=self.retrieve_password)
        self.retrieve_button.grid(row=0, column=2, padx=5)

        self.view_all_button = ttk.Button(button_frame, text="📜 View All", bootstyle="info", command=self.view_all_passwords)
        self.view_all_button.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(button_frame, text="🗑 Delete", bootstyle="danger", command=self.delete_password)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

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

    # Load theme preference
    def load_theme(self):
        if os.path.exists(THEME_FILE):
            with open(THEME_FILE, "r") as file:
                return json.load(file).get("theme", "darkly")
        return "darkly"

    # Save theme preference
    def save_theme(self):
        with open(THEME_FILE, "w") as file:
            json.dump({"theme": self.current_theme}, file)

    # Toggle between light and dark mode
    def toggle_theme(self):
        self.current_theme = "litera" if self.current_theme == "darkly" else "darkly"
        self.save_theme()
        self.root.destroy()
        main(self.current_theme)

# Run the GUI
def main(theme="darkly"):
    master_password = simpledialog.askstring("🔑 Master Password", "Enter your master password:", show="*")
    if master_password:
        manager = PasswordManager(master_password)
        root = ttk.Window(themename=theme)  # Apply selected theme
        app = PasswordManagerGUI(root, manager)
        root.mainloop()
    else:
        messagebox.showerror("Error", "Master password is required!")

if __name__ == "__main__":
    main()
