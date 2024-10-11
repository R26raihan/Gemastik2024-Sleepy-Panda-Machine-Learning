import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def parse_phone_number(phone_number, region='ID'):
    try:
        parsed_number = phonenumbers.parse(phone_number, region)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number"
        
        number_info = {
            "international_format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "national_format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
            "E164_format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "country_code": parsed_number.country_code,
            "national_number": parsed_number.national_number,
            "location": geocoder.description_for_number(parsed_number, "en"),
            "carrier": carrier.name_for_number(parsed_number, "en"),
            "timezones": timezone.time_zones_for_number(parsed_number)
        }

        return number_info

    except phonenumbers.NumberParseException as e:
        return f"Error parsing phone number: {e}"

# Example usage:
phone_number = "+6285873109552"
info = parse_phone_number(phone_number)
print(info)
