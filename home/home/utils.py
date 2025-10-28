from datetime import date
from home.models import HolidayClosure

def is_restaurant_closed_on_holiday(date_to_check: date) -> bool:
    """
    Returns True if the restaurant is closed on the given date
    due to a full-day holiday closure, otherwise False.
    """
    return HolidayClosure.objects.filter(
        date=date_to_check,
        is_full_day_closure=True
    ).exists()
