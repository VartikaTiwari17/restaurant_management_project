from django.db import models
from django.utils import timezone

class PromotionalOfferManager(models.Manager):
    def upcoming_offers(self):
        today = timezone.now().date()
        return self.filter(
            is_active=True,
            start_date__lte=today,
            end_date__gte=today
        )
