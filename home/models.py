from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_vegetarian = models.BooleanField(default=False)  # 👈 New field

    def __str__(self):
        return self.name
