import datetime

def format_timedelta_human_readable(delta: datetime.timedelta) -> str:
    total_seconds = int(delta.total_seconds())
    
    # If timedelta is 0
    if total_seconds == 0:
        return "0 minutes"

    days, remainder = divmod(total_seconds, 86400)  # 86400 = seconds in a day
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)

    parts = []

    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

    return " ".join(parts)
