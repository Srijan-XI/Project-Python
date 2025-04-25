import math

def binary_to_decimal(binary):
    decimal, base = 0, 1
    while binary > 0:
        decimal += (binary % 10) * base
        binary //= 10
        base *= 2
    return decimal

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def hex_to_decimal(hex_num):
    return int(hex_num, 16)

def decimal_to_hex(decimal):
    return hex(decimal)[2:].upper()

def octal_to_decimal(octal):
    return int(str(octal), 8)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error: Division by zero!" if b == 0 else a / b

def main():
    print("Main Menu:\n1. Calculator\n2. Number Conversion")
    main_choice = int(input("Enter your choice: "))
    
    if main_choice == 1:
        print("\nCalculator Menu:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        calc_choice = int(input("Enter your choice: "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        operations = {1: add, 2: subtract, 3: multiply, 4: divide}
        print("Result:", operations.get(calc_choice, lambda x, y: "Invalid choice!")(num1, num2))
    
    elif main_choice == 2:
        print("\nNumber Conversion Menu:\n1. Binary to Decimal\n2. Decimal to Binary\n3. Decimal to Octal\n4. Hexadecimal to Decimal\n5. Octal to Decimal\n6. Decimal to Hexadecimal")
        conv_choice = int(input("Enter your choice: "))
        
        if conv_choice == 1:
            binary = int(input("Enter a binary number: "))
            print(f"{binary} in binary = {binary_to_decimal(binary)} in decimal")
        elif conv_choice == 2:
            decimal = int(input("Enter a decimal number: "))
            print(f"{decimal} in decimal = {decimal_to_binary(decimal)} in binary")
        elif conv_choice == 3:
            decimal = int(input("Enter a decimal number: "))
            print(f"{decimal} in decimal = {decimal_to_octal(decimal)} in octal")
        elif conv_choice == 4:
            hex_num = input("Enter a hexadecimal number: ")
            print(f"{hex_num} in hexadecimal = {hex_to_decimal(hex_num)} in decimal")
        elif conv_choice == 5:
            octal = int(input("Enter an octal number: "))
            print(f"{octal} in octal = {octal_to_decimal(octal)} in decimal")
        elif conv_choice == 6:
            decimal = int(input("Enter a decimal number: "))
            print(f"{decimal} in decimal = {decimal_to_hex(decimal)} in hexadecimal")
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
