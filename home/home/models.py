# home/models.py
from django.db import models

class DailyOperatingHours(models.Model):
    day = models.CharField(max_length=10, unique=True)  # e.g. Monday, Tuesday
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.opening_time} - {self.closing_time}"
