from django.db import models # type: ignore

class VegetarianMenuItemManager(models.Manager):
    def get_vegetarian_items(self):
        return super().get_queryset().filter(is_vegetarian=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    preparation_time_minutes = models.IntegerField(blank=True, null=True)

    # ✅ Add the custom manager
    objects = models.Manager()  # Default manager
    vegetarian_objects = VegetarianMenuItemManager()  # Custom vegetarian manager

    def __str__(self):
        return self.name
