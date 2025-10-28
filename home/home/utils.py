from datetime import datetime

def calculate_duration_in_minutes(start_time: datetime, end_time: datetime) -> int:
    """
    Calculate the total duration between two datetime objects in minutes.
    Returns an integer.
    """
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise ValueError("Both inputs must be datetime objects.")

    duration = end_time - start_time
    total_minutes = int(duration.total_seconds() // 60)
    return total_minutes
