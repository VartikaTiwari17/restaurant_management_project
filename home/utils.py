touch home/utils.py
from datetime import datetime, timedelta
from django.utils import timezone
from home.models import DailyOperatingHours


def get_time_until_next_opening(current_datetime=None):
    """
    Returns a message like:
    - "Opens in 2 hours 30 minutes"
    - "Opens on Monday at 9:00 AM"
    or None if no future openings found.
    """

    if current_datetime is None:
        current_datetime = timezone.localtime()

    # Normalize to current local time
    current_day = current_datetime.weekday()  # Monday = 0, Sunday = 6

    # Fetch all schedule entries
    operating_hours = DailyOperatingHours.objects.all().order_by('day_of_week')

    if not operating_hours.exists():
        return None

    # Check current and next 7 days
    for i in range(8):
        check_day = (current_day + i) % 7
        day_hours = operating_hours.filter(day_of_week=check_day).first()

        if not day_hours:
            continue

        open_time = day_hours.open_time
        close_time = day_hours.close_time

        # Build full datetime for comparison
        check_date = (current_datetime + timedelta(days=i)).date()
        open_datetime = datetime.combine(check_date, open_time).replace(tzinfo=current_datetime.tzinfo)
        close_datetime = datetime.combine(check_date, close_time).replace(tzinfo=current_datetime.tzinfo)

        # If today but not yet open
        if i == 0 and current_datetime < open_datetime:
            time_diff = open_datetime - current_datetime
            hours, remainder = divmod(time_diff.seconds, 3600)
            minutes = remainder // 60
            return f"Opens in {hours} hours {minutes} minutes"

        # If future day
        if i > 0:
            weekday_name = open_datetime.strftime("%A")
            formatted_time = open_datetime.strftime("%I:%M %p").lstrip("0")
            return f"Opens on {weekday_name} at {formatted_time}"

    return None
