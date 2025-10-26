from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # New field added

    objects = models.Manager()  # Default manager (or custom manager if any)

    def __str__(self):
        return self.name
