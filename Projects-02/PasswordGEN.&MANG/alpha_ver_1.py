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

# Password Manager Class with Encryption
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
                    print("\n❌ Incorrect master password or corrupted file.\n")
                    return {}
        return {}

    def save_passwords(self):
        encrypted_data = self.cipher.encrypt(json.dumps(self.passwords).encode())
        with open(self.filename, "w") as file:
            file.write(encrypted_data.decode())

    def add_password(self, site, username, password):
        self.passwords[site] = {"username": username, "password": password}
        self.save_passwords()
        print(f"\n✅ Password for {site} saved securely!\n")

    def get_password(self, site):
        if site in self.passwords:
            return self.passwords[site]
        return "❌ No password found for this site."

    def view_all(self):
        if not self.passwords:
            print("\n🔍 No passwords saved yet.\n")
        else:
            print("\n🔐 Saved Accounts:\n")
            for site, credentials in self.passwords.items():
                print(f"📌 {site} -> Username: {credentials['username']}, Password: {credentials['password']}")
            print()

    def delete_password(self, site):
        if site in self.passwords:
            del self.passwords[site]
            self.save_passwords()
            print(f"\n🗑️ Password for {site} deleted securely!\n")
        else:
            print("\n❌ No password found for this site.\n")

# Menu for User Interaction
def main():
    master_password = input("\n🔑 Enter your master password: ")
    manager = PasswordManager(master_password)

    while True:
        print("\n🔐 PASSWORD MANAGER MENU")
        print("1️⃣  Generate a Password")
        print("2️⃣  Save a Password")
        print("3️⃣  Retrieve a Password")
        print("4️⃣  View All Saved Passwords")
        print("5️⃣  Delete a Password")
        print("6️⃣  Exit")

        choice = input("\nSelect an option (1-6): ")

        if choice == "1":
            length = int(input("\nEnter password length: "))
            print(f"\n🆕 Generated Password: {generate_password(length)}\n")

        elif choice == "2":
            site = input("\nEnter website name: ")
            username = input("Enter username: ")
            password = generate_password(20)
            manager.add_password(site, username, password)

        elif choice == "3":
            site = input("\nEnter website name: ")
            print(manager.get_password(site))

        elif choice == "4":
            manager.view_all()

        elif choice == "5":
            site = input("\nEnter website name to delete: ")
            manager.delete_password(site)

        elif choice == "6":
            print("\n🔒 Exiting Password Manager. Stay safe!\n")
            break

        else:
            print("\n❌ Invalid choice! Please select a valid option.\n")

# Run the Secure Password Manager
if __name__ == "__main__":
    main()
