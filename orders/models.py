from django.db import models
from django.core.exceptions import ValidationError
from home.models import Table  # assuming Table model is in home/models.py


class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()

    def clean(self):
        """
        Custom validation to ensure the number of guests does not exceed table capacity.
        """
        if self.table and self.number_of_guests:
            if self.number_of_guests > self.table.max_capacity:
                raise ValidationError(
                    {"number_of_guests": "Number of guests exceeds the capacity of the selected table."}
                )

    def __str__(self):
        return f"Reservation for {self.customer_name} on {self.reservation_date} at {self.reservation_time}"
