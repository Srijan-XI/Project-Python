<<<<<<< HEAD
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

password_length = int(input("Enter the password length: "))
password = generate_password(password_length)
print("Generated Password:", password)
=======
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

password_length = int(input("Enter the password length: "))
password = generate_password(password_length)
print("Generated Password:", password)
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
