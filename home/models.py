from django.db import models
from django.utils import timezone

class ReservationManager(models.Manager):
    def get_upcoming_reservations(self):
        """
        Returns reservations scheduled for a future date and time.
        """
        now = timezone.now()
        return self.filter(reservation_datetime__gt=now)
