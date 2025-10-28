import datetime
from django.db import models

class DailySpecialManager(models.Manager):
    def upcoming(self):
        """Return specials for today or future dates."""
        today = datetime.date.today()
        return self.filter(date__gte=today)

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    objects = DailySpecialManager()  # Attach the custom manager

    def __str__(self):
        return f"{self.name} - {self.date}"
