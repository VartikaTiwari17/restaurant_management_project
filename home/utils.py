import re

def is_valid_phone_number(phone_number: str) -> bool:
    """
    Validates a phone number string.
    Returns True if it matches a basic valid pattern (10–12 digits),
    optionally allowing spaces, hyphens, or a '+' country code.
    """
    pattern = r'^\+?\d[\d\s\-]{8,14}\d$'
    return bool(re.match(pattern, phone_number))
