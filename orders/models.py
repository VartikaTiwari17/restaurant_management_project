from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
