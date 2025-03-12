import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Taking input from user
number = input("Enter Phone Number with +__: ")

# Parsing the phone number
phone = phonenumbers.parse(number)

# Getting phone number details
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, "en")

# Displaying the results
print(f"Phone Number: {number}")
print(f"Time Zone: {time}")
print(f"Carrier: {car}")
print(f"Region: {reg}")

