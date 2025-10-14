import re

def normalize_phone(phone_number):
    clean_number = re.sub(r'[^0-9+]', '', phone_number)

    if clean_number.startswith('+380'):
        return clean_number

    elif clean_number.startswith('380'):
        return '+' + clean_number

    elif not clean_number.startswith('+'):
        return '+38' + clean_number

    return clean_number

print(normalize_phone(" 093tf6rxdsud756436 "))   

