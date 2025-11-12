from django.db import models

class MenuItemManager(models.Manager):
    def get_by_price_range(self, min_price, max_price):
        """Return menu items within the specified price range."""
        return self.filter(price__gte=min_price, price__lte=max_price)


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    # ... other existing fields ...

    # Attach the custom manager
    objects = MenuItemManager()

    def __str__(self):
        return self.name
