from datetime import datetime

def format_datetime(dt):
    """
    Formats a datetime object into a readable string.
    Example: 'January 1, 2023 at 10:30 AM'
    Returns an empty string if dt is None.
    """
    if dt is None:
        return ""
    
    return dt.strftime("%B %d, %Y at %I:%M %p")
