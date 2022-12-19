import phonenumbers
from phonenumbers import geocoder

lang = "en"

number = input("Number with country code\n")

phone_number = phonenumbers.parse(number)
location = geocoder.description_for_number(phone_number, lang)

print(f"Location number: {location}")

