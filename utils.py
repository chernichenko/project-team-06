import re

def validate_phone(phone):
    pattern = re.compile(r'^\+?\d{10,15}$')
    return bool(pattern.match(phone))

def validate_email(email):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(pattern.match(email))
