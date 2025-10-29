from django.db import models

class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)
    max_seats = models.IntegerField(default=4)  # 🆕 added field

    def __str__(self):
        return f"Table {self.table_number} (Seats: {self.max_seats})"
