# Install dependencies before running the script:
# pip install qrcode[pil] python-barcode
try:
    import qrcode
except ImportError:
    print("Error: 'qrcode' module not installed. Please run: pip install qrcode[pil]")
    exit()

try:
    import barcode
    from barcode.writer import ImageWriter
except ImportError:
    print("Error: 'python-barcode' module not installed. Please run: pip install python-barcode[images]")
    exit()

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    logging.info(f"✅ QR code saved as {filename}")

def generate_barcode(data, filename="barcode.png"):
    try:
        barcode_format = barcode.get_barcode_class('code128')
        code = barcode_format(data, writer=ImageWriter())
        saved_path = code.save(filename.rsplit(".", 1)[0])
        logging.info(f"✅ Barcode saved as {saved_path}")
    except barcode.errors.BarcodeError as e:
        logging.error(f"❌ Barcode generation failed: {e}")

def main():
    print("\n🔐 Secure Encoder Tool")
    print("1️⃣ Generate QR Code")
    print("2️⃣ Generate Barcode\n")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    data = input("Enter the data for encoding: ").strip()

    if choice == "1":
        generate_qr(data)
    elif choice == "2":
        generate_barcode(data)
    else:
        logging.error("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
