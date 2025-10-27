from django.db import models
from django.utils import timezone

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    date = models.DateField(default=timezone.now().date)

    def __str__(self):
        return f"{self.name} ({self.date})"
