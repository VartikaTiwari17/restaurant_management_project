from django.db import models

class AvailableMenuItemManager(models.Manager):
    def get_available_items(self):
        return self.filter(is_available=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()  # Default manager
    available = AvailableMenuItemManager()  # Custom manager

    def __str__(self):
        return self.name
