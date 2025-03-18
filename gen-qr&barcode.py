# Install dependencies before running the script:
# pip install qrcode[pil] python-barcode
import qrcode
import barcode
from barcode.writer import ImageWriter

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved as {filename}")

def generate_barcode(data, filename="barcode.png"):
    barcode_format = barcode.get_barcode_class('code128')  # Code 128 format
    code = barcode_format(data, writer=ImageWriter())
    code.save(filename.split(".")[0])  # Barcode library automatically adds format extensions
    print(f"Barcode saved as {filename}")

def main():
    print("Select an option:")
    print("1. Generate QR Code")
    print("2. Generate Barcode")
    
    choice = input("Enter 1 or 2: ")
    data = input("Enter the data for encoding: ")

    if choice == "1":
        generate_qr(data)
    elif choice == "2":
        generate_barcode(data)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
