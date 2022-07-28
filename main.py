# This is a simple code of a Python script that can be run to find details of a phone number.
# Copyright (c) 2022 Vaibhav Ganeriwala

# import the necessary packages
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# get the phone number from the user
phone_number = input("Enter the phone number in international format (like +919XXXXXXXXX): ")

# defining the function
def get_details(phone_number):
    # get the phone number from the user
    phone = phonenumbers.parse(phone_number)
    
    # location of the phone number
    print("Location : " + geocoder.description_for_number(phone, "en"))

    # get the carrier of the phone number
    print("Carrier : " + carrier.name_for_number(phone, "en"))

    # get the timezone of the phone number
    print("Timezone : ", timezone.time_zones_for_number(phone))

    # get the region information
    print("Region : ", phonenumbers.region_code_for_number(phone))


# calling the function
get_details(phone_number)