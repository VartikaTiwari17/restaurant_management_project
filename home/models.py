from django.db import models

# ✅ Custom Manager
class VegetarianMenuItemManager(models.Manager):
    def get_queryset(self):
        # Returns only vegetarian menu items
        return super().get_queryset().filter(is_vegetarian=True)

# ✅ MenuItem Model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_vegetarian = models.BooleanField(default=False)

    # Default manager (all items)
    objects = models.Manager()
    # Custom manager (vegetarian-only)
    vegetarian = VegetarianMenuItemManager()

    def __str__(self):
        return self.name
