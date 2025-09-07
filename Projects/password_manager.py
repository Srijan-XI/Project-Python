<<<<<<< HEAD
from cryptography.fernet import Fernet
import json
import os

# File to store passwords
PASSWORD_FILE = "passwords.json"
KEY_FILE = "secret.key"

# Generate or load encryption key
def load_key():
    """Load the encryption key from a file or generate a new one if not found."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt password
def encrypt_password(password, key):
    """Encrypts a password using Fernet encryption."""
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password, key):
    """Decrypts an encrypted password using Fernet."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Load stored passwords
def load_passwords():
    """Loads saved passwords from the JSON file. Returns an empty dictionary if file does not exist."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

# Save updated password data
def save_passwords(passwords):
    """Saves password data to the JSON file in a readable format."""
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# Add a new service without a password
def add_service(service):
    """Adds a new service entry without a password."""
    passwords = load_passwords()
    if service in passwords:
        print("⚠️ Service already exists.")
    else:
        passwords[service] = {"username": "", "password": ""}
        save_passwords(passwords)
        print(f"✅ Service '{service}' added successfully!")

# Remove a service completely
def remove_service(service):
    """Removes a service and its associated credentials from storage."""
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"🗑️ Service '{service}' removed successfully.")
    else:
        print("❌ Service not found.")

# Save or update password
def save_password(service, username, password):
    """Saves or updates a password for a given service."""
    key = load_key()
    passwords = load_passwords()

    passwords[service] = {
        "username": username,
        "password": encrypt_password(password, key)
    }

    save_passwords(passwords)
    print(f"✅ Password saved for {service}!")

# Retrieve password
def get_password(service):
    """Retrieves and decrypts the password for a given service."""
    key = load_key()
    passwords = load_passwords()

    if service in passwords:
        username = passwords[service]["username"]
        encrypted_password = passwords[service]["password"]
        if encrypted_password:
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"🔑 Service: {service}\n👤 Username: {username}\n🔒 Password: {decrypted_password}")
        else:
            print(f"🔹 Service '{service}' exists but no password is saved.")
    else:
        print("❌ Service not found.")

# List all saved services
def list_services():
    """Lists all saved services in the password manager."""
    passwords = load_passwords()
    if passwords:
        print("\n🔹 Saved Services:")
        for service in passwords.keys():
            print(f"- {service}")
    else:
        print("❌ No saved services yet.")

# User menu
def main():
    """Runs the interactive menu for the password manager."""
    while True:
        print("\n🔐 Password Manager")
        print("1️⃣ Add New Service")
        print("2️⃣ Remove Service")
        print("3️⃣ Save/Update Password")
        print("4️⃣ Retrieve Password")
        print("5️⃣ List All Services")
        print("6️⃣ Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            service = input("Enter new service name: ").strip()
            if service:
                add_service(service)
            else:
                print("❌ Service name cannot be empty.")
        elif choice == "2":
            service = input("Enter service name to remove: ").strip()
            remove_service(service)
        elif choice == "3":
            service = input("Enter service name: ").strip()
            if service in load_passwords():
                username = input("Enter username/email: ").strip()
                password = input("Enter password: ").strip()
                if username and password:
                    save_password(service, username, password)
                else:
                    print("❌ Fields cannot be empty.")
            else:
                print("❌ Service not found. Add the service first.")
        elif choice == "4":
            service = input("Enter service name: ").strip()
            get_password(service)
        elif choice == "5":
            list_services()
        elif choice == "6":
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
=======
from cryptography.fernet import Fernet
import json
import os

# File to store passwords
PASSWORD_FILE = "passwords.json"
KEY_FILE = "secret.key"

# Generate or load encryption key
def load_key():
    """Load the encryption key from a file or generate a new one if not found."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt password
def encrypt_password(password, key):
    """Encrypts a password using Fernet encryption."""
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password, key):
    """Decrypts an encrypted password using Fernet."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Load stored passwords
def load_passwords():
    """Loads saved passwords from the JSON file. Returns an empty dictionary if file does not exist."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

# Save updated password data
def save_passwords(passwords):
    """Saves password data to the JSON file in a readable format."""
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# Add a new service without a password
def add_service(service):
    """Adds a new service entry without a password."""
    passwords = load_passwords()
    if service in passwords:
        print("⚠️ Service already exists.")
    else:
        passwords[service] = {"username": "", "password": ""}
        save_passwords(passwords)
        print(f"✅ Service '{service}' added successfully!")

# Remove a service completely
def remove_service(service):
    """Removes a service and its associated credentials from storage."""
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"🗑️ Service '{service}' removed successfully.")
    else:
        print("❌ Service not found.")

# Save or update password
def save_password(service, username, password):
    """Saves or updates a password for a given service."""
    key = load_key()
    passwords = load_passwords()

    passwords[service] = {
        "username": username,
        "password": encrypt_password(password, key)
    }

    save_passwords(passwords)
    print(f"✅ Password saved for {service}!")

# Retrieve password
def get_password(service):
    """Retrieves and decrypts the password for a given service."""
    key = load_key()
    passwords = load_passwords()

    if service in passwords:
        username = passwords[service]["username"]
        encrypted_password = passwords[service]["password"]
        if encrypted_password:
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"🔑 Service: {service}\n👤 Username: {username}\n🔒 Password: {decrypted_password}")
        else:
            print(f"🔹 Service '{service}' exists but no password is saved.")
    else:
        print("❌ Service not found.")

# List all saved services
def list_services():
    """Lists all saved services in the password manager."""
    passwords = load_passwords()
    if passwords:
        print("\n🔹 Saved Services:")
        for service in passwords.keys():
            print(f"- {service}")
    else:
        print("❌ No saved services yet.")

# User menu
def main():
    """Runs the interactive menu for the password manager."""
    while True:
        print("\n🔐 Password Manager")
        print("1️⃣ Add New Service")
        print("2️⃣ Remove Service")
        print("3️⃣ Save/Update Password")
        print("4️⃣ Retrieve Password")
        print("5️⃣ List All Services")
        print("6️⃣ Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            service = input("Enter new service name: ").strip()
            if service:
                add_service(service)
            else:
                print("❌ Service name cannot be empty.")
        elif choice == "2":
            service = input("Enter service name to remove: ").strip()
            remove_service(service)
        elif choice == "3":
            service = input("Enter service name: ").strip()
            if service in load_passwords():
                username = input("Enter username/email: ").strip()
                password = input("Enter password: ").strip()
                if username and password:
                    save_password(service, username, password)
                else:
                    print("❌ Fields cannot be empty.")
            else:
                print("❌ Service not found. Add the service first.")
        elif choice == "4":
            service = input("Enter service name: ").strip()
            get_password(service)
        elif choice == "5":
            list_services()
        elif choice == "6":
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
