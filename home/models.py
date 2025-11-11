from django.db import models


# Custom Manager for Vegetarian Menu Items
class VegetarianMenuItemManager(models.Manager):
    def get_vegetarian_items(self):
        """Return only vegetarian menu items."""
        return self.filter(is_vegetarian=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(default=0, help_text="Current available stock of this item")

    # Default Manager
    objects = models.Manager()

    # Custom Vegetarian Manager
    vegetarian_objects = VegetarianMenuItemManager()

    def __str__(self):
        return self.name
