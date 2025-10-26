from django.db import models

# Custom manager for MenuItem
class MenuItemManager(models.Manager):
    def get_budget_items(self, max_price):
        """
        Returns MenuItem queryset filtered by price less than max_price
        """
        return self.filter(price__lte=max_price)

# Assuming MenuItem model exists
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_featured = models.BooleanField(default=False)

    objects = MenuItemManager()  # Attach custom manager

    def __str__(self):
        return self.name
