from datetime import datetime
from .models import DailyOperatingHours

def is_restaurant_open() -> bool:
    """
    Determines if the restaurant is currently open based on DailyOperatingHours.
    
    Returns:
        bool: True if open, False if closed.
    """
    now = datetime.now()
    current_day = now.strftime('%A')  # e.g., 'Monday'
    current_time = now.time()

    try:
        hours = DailyOperatingHours.objects.get(day_of_week=current_day)
        if hours.opening_time <= current_time <= hours.closing_time:
            return True
        else:
            return False
    except DailyOperatingHours.DoesNotExist:
        # No operating hours defined for today
        return False
