from django.db import models

class MenuItemManager(models.Manager):
    def get_vegetarian_items(self):
        return self.filter(is_vegetarian=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)

    # Replace default manager
    objects = MenuItemManager()

    def __str__(self):
        return self.name
