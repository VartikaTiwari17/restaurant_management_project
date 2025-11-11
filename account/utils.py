import random
import string

def generate_random_password(length=12):
    """
    Generate a secure random password with the given length.
    Includes uppercase, lowercase, digits, and special characters.
    """

    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")

    # Define all character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_chars = upper + lower + digits + special

    # Ensure the password includes at least one character from each type
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining characters randomly
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)
