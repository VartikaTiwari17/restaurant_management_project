touch home/utils.py
from datetime import datetime, timedelta

def format_time_ago(timestamp):
    """
    Converts a datetime object into a human-readable 'time ago' format.
    Example: '5 minutes ago', '2 days ago', 'just now'
    """
    if not timestamp:
        return "unknown time"

    now = datetime.now(timestamp.tzinfo) if timestamp.tzinfo else datetime.now()
    diff = now - timestamp

    seconds = diff.total_seconds()
    minutes = int(seconds // 60)
    hours = int(minutes // 60)
    days = int(hours // 24)
    weeks = int(days // 7)
    months = int(days // 30)
    years = int(days // 365)

    if seconds < 60:
        return "just now"
    elif minutes == 1:
        return "1 minute ago"
    elif minutes < 60:
        return f"{minutes} minutes ago"
    elif hours == 1:
        return "1 hour ago"
    elif hours < 24:
        return f"{hours} hours ago"
    elif days == 1:
        return "1 day ago"
    elif days < 7:
        return f"{days} days ago"
    elif weeks == 1:
        return "1 week ago"
    elif weeks < 5:
        return f"{weeks} weeks ago"
    elif months == 1:
        return "1 month ago"
    elif months < 12:
        return f"{months} months ago"
    elif years == 1:
        return "1 year ago"
    else:
        return f"{years} years ago"
