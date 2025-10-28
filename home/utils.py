from datetime import datetime
from home.models import DailyOperatingHours

def get_today_operating_hours():
    """
    Returns today's operating hours as a tuple: (open_time, close_time).
    If the restaurant is closed or no entry is found, returns (None, None).
    """
    # Get current day name (e.g., 'Monday')
    today = datetime.now().strftime('%A')

    # Try to find the entry for today's day
    try:
        operating_hours = DailyOperatingHours.objects.get(day_of_week=today)
        return (operating_hours.open_time, operating_hours.close_time)
    except DailyOperatingHours.DoesNotExist:
        return (None, None)
