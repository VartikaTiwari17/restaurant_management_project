from datetime import datetime, timezone

def get_review_age(created_at):
    """
    Returns a human-readable string representing how long ago the review was posted.
    Example: 'just now', '5 minutes ago', '2 hours ago', '3 days ago', etc.
    """
    now = datetime.now(timezone.utc)
    diff = now - created_at
    seconds = diff.total_seconds()

    # Define time intervals
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    months = days / 30
    years = days / 365

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        return f"{int(minutes)} minute{'s' if minutes >= 2 else ''} ago"
    elif hours < 24:
        return f"{int(hours)} hour{'s' if hours >= 2 else ''} ago"
    elif days < 7:
        return f"{int(days)} day{'s' if days >= 2 else ''} ago"
    elif weeks < 4:
        return f"{int(weeks)} week{'s' if weeks >= 2 else ''} ago"
    elif months < 12:
        return f"{int(months)} month{'s' if months >= 2 else ''} ago"
    else:
        return f"{int(years)} year{'s' if years >= 2 else ''} ago"
