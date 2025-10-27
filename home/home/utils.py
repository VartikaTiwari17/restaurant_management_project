# home/utils.py
from datetime import datetime
from django.utils import timezone
from .models import DailyOperatingHours  # make sure this model exists

def is_restaurant_open():
    """Return True if the restaurant is currently open, else False."""
    now = timezone.localtime()
    current_day = now.strftime('%A')  # e.g., 'Monday'
    current_time = now.time()

    try:
        today_hours = DailyOperatingHours.objects.get(day=current_day)
    except DailyOperatingHours.DoesNotExist:
        return False  # No data for today means closed

    # Check if within today's operating hours
    if today_hours.opening_time <= current_time <= today_hours.closing_time:
        return True
    return False
