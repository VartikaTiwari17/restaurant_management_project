import re

def sanitize_text(text: str) -> str:
    """
    Cleans up the given text by:
    - Stripping leading and trailing whitespace
    - Replacing multiple spaces with a single space
    """
    if not isinstance(text, str):
        return text  # In case a non-string is passed accidentally
    
    # Remove leading/trailing whitespace
    cleaned_text = text.strip()
    
    # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    return cleaned_text
