import re

# validate phone number
def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.fullmatch(pattern, phone):
        return True
    else:
        return False


# validate SSN
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False


# validate zip code
def validate_zip(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False


def main():

    phone = input("Enter phone number (123-456-7890): ")
    ssn = input("Enter SSN (123-45-6789): ")
    zipcode = input("Enter ZIP code (12345 or 12345-6789): ")

    print()

    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

    if validate_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is invalid")

    if validate_zip(zipcode):
        print("ZIP code is valid")
    else:
        print("ZIP code is invalid")


main()
