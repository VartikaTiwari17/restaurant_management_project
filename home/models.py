from django.db import models

class Table(models.Model):
    table_number = models.CharField(max_length=20, unique=True)  # Unique table identifier
    capacity = models.PositiveIntegerField()                      # Max guests
    is_available = models.BooleanField(default=True)              # Availability status

    def __str__(self):
        return f"{self.table_number} (Seats: {self.capacity})"
