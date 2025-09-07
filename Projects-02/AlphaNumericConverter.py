<<<<<<< HEAD
def convert_input(input_str):
    result = []

    for item in input_str.split():
        if item.isalpha():
            # Convert letters to numbers
            for char in item.upper():
                if 'A' <= char <= 'Z':
                    result.append(str(ord(char) - ord('A') + 1))
        elif item.isdigit():
            # Convert numbers to letters
            num = int(item)
            if 1 <= num <= 26:
                result.append(chr(num + ord('A') - 1))
            else:
                result.append('?')  # Invalid number for alphabet
        else:
            result.append('?')  # Invalid character

    return ' '.join(result)

def store_in_file(conversion_result, filename="conversion_result.txt"):
    with open(filename, 'w') as file:
        file.write(conversion_result)
    print(f"Conversion result has been stored in {filename}")

# Example usage:
input_data = input("Enter letters or numbers (space-separated): ")
converted = convert_input(input_data)

# Store the result in a text file
store_in_file(converted)
print("Converted Output:", converted)
=======
def convert_input(input_str):
    result = []

    for item in input_str.split():
        if item.isalpha():
            # Convert letters to numbers
            for char in item.upper():
                if 'A' <= char <= 'Z':
                    result.append(str(ord(char) - ord('A') + 1))
        elif item.isdigit():
            # Convert numbers to letters
            num = int(item)
            if 1 <= num <= 26:
                result.append(chr(num + ord('A') - 1))
            else:
                result.append('?')  # Invalid number for alphabet
        else:
            result.append('?')  # Invalid character

    return ' '.join(result)

def store_in_file(conversion_result, filename="conversion_result.txt"):
    with open(filename, 'w') as file:
        file.write(conversion_result)
    print(f"Conversion result has been stored in {filename}")

# Example usage:
input_data = input("Enter letters or numbers (space-separated): ")
converted = convert_input(input_data)

# Store the result in a text file
store_in_file(converted)
print("Converted Output:", converted)
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
