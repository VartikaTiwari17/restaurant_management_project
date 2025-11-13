from django.db import models

class VegetarianMenuItemManager(models.Manager):
    def get_queryset(self):
        # Return only vegetarian items
        return super().get_queryset().filter(is_vegetarian=True)
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    # ... other fields ...

    # Custom manager for vegetarian items
    vegetarian_objects = VegetarianMenuItemManager()

    def __str__(self):
        return self.name
