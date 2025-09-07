<<<<<<< HEAD
import phonenumbers
import re
from phonenumbers import carrier, geocoder, timezone

def validate_input(number):
    """Check if the input matches a phone number pattern."""
    pattern = r'^\+\d{1,3}\s?\d{6,14}$'  # Country code + Number
    return re.match(pattern, number)

def get_phone_details():
    while True:
        mobile_no = input("\nEnter Phone number with country code (+XX XXXXXXXXXX) or 'exit' to quit: ").strip()
        
        if mobile_no.lower() == "exit":
            print("\nExiting program. Have a great day! 😊")
            break

        if not validate_input(mobile_no):
            print("⚠️ Invalid format! Please enter a valid phone number (e.g., +1 1234567890).")
            continue

        try:
            parsed_no = phonenumbers.parse(mobile_no)
            if phonenumbers.is_valid_number(parsed_no):
                print("\n✅ Phone Number Details:")
                print(f"📍 Region: {', '.join(timezone.time_zones_for_number(parsed_no))}")
                print(f"📡 Service Provider: {carrier.name_for_number(parsed_no, 'en') or 'Unknown'}")
                print(f"🌍 Country: {geocoder.description_for_number(parsed_no, 'en') or 'Unknown'}")
            else:
                print("❌ Invalid phone number! Please try again.")
        except phonenumbers.phonenumberutil.NumberParseException:
            print("⚠️ Error parsing the number. Ensure it includes the country code.")

if __name__ == "__main__":
    get_phone_details()
=======
import phonenumbers
import re
from phonenumbers import carrier, geocoder, timezone

def validate_input(number):
    """Check if the input matches a phone number pattern."""
    pattern = r'^\+\d{1,3}\s?\d{6,14}$'  # Country code + Number
    return re.match(pattern, number)

def get_phone_details():
    while True:
        mobile_no = input("\nEnter Phone number with country code (+XX XXXXXXXXXX) or 'exit' to quit: ").strip()
        
        if mobile_no.lower() == "exit":
            print("\nExiting program. Have a great day! 😊")
            break

        if not validate_input(mobile_no):
            print("⚠️ Invalid format! Please enter a valid phone number (e.g., +1 1234567890).")
            continue

        try:
            parsed_no = phonenumbers.parse(mobile_no)
            if phonenumbers.is_valid_number(parsed_no):
                print("\n✅ Phone Number Details:")
                print(f"📍 Region: {', '.join(timezone.time_zones_for_number(parsed_no))}")
                print(f"📡 Service Provider: {carrier.name_for_number(parsed_no, 'en') or 'Unknown'}")
                print(f"🌍 Country: {geocoder.description_for_number(parsed_no, 'en') or 'Unknown'}")
            else:
                print("❌ Invalid phone number! Please try again.")
        except phonenumbers.phonenumberutil.NumberParseException:
            print("⚠️ Error parsing the number. Ensure it includes the country code.")

if __name__ == "__main__":
    get_phone_details()
>>>>>>> 397691e3bddc1c2468c0790a7ae5dcc8aba4e6c3
