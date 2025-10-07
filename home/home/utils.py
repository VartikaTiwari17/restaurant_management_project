import re 

def is_valid_email(email: str) -> bool:
    """
    Validate an email address using regex.
    Returns True if the email is valid, False otherwise.
    """



    # Basic email regex pattern 
    email_regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


    # Check if the email matches the pattern
    return re.match(email_regex, email) is not None