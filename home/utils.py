from django.utils import timezone
from home.models import DailySpecial

def get_today_special():
    """Return today's Daily Special if available, else None."""
    today = timezone.now().date()
    special = DailySpecial.objects.filter(date=today).first()
    return special
