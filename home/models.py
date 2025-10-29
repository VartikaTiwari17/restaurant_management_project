from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_spicy = models.BooleanField(default=False, null=True, blank=True)  # 🌶️ new field

    def __str__(self):
        return self.name
