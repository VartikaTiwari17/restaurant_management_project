from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    opening_hours = models.CharField(
        max_length=50,
        help_text="Format example: 11:00 AM - 11:00 PM (EST)"
    )


     def __str__(self):
        return self.name