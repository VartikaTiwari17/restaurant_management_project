from django.db import models

# ✅ Custom Manager
class MenuItemManager(models.Manager):
    def vegetarian_items(self):
        # Return only vegetarian menu items
        return self.filter(is_vegetarian=True)


# ✅ MenuItem Model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_vegetarian = models.BooleanField(default=False)

    # Attach the custom manager
    objects = MenuItemManager()

    def __str__(self):
        return self.name
