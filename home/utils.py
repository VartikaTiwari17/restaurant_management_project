from datetime import datetime
from home.models import DailyOperatingHours

def is_valid_reservation_time(reservation_datetime):
    """
    Check if the given reservation time is valid based on the restaurant's
    operating hours for that specific day.

    Args:
        reservation_datetime (datetime): The proposed reservation time.

    Returns:
        bool: True if the time is within open and close hours, False otherwise.
    """
    if reservation_datetime is None:
        return False

    # Get weekday name, e.g., 'Monday'
    weekday_name = reservation_datetime.strftime('%A')

    try:
        # Fetch today's operating hours
        operating_hours = DailyOperatingHours.objects.get(day=weekday_name)

        if not operating_hours.open_time or not operating_hours.close_time:
            return False

        # Extract just the time part
        proposed_time = reservation_datetime.time()

        return operating_hours.open_time < proposed_time < operating_hours.close_time

    except DailyOperatingHours.DoesNotExist:
        return False
