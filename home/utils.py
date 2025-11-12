from datetime import date
from home.models import HolidayHours  # adjust import path if HolidayHours is elsewhere

def check_reservation_holiday_conflict(reservation_date: date) -> bool:
    """
    Checks whether a given reservation_date falls on a restaurant holiday.
    Returns True if the restaurant is closed that day, otherwise False.
    """
    # Check if a HolidayHours entry exists for the given date
    conflict_exists = HolidayHours.objects.filter(date=reservation_date).exists()
    return conflict_exists
