from django.db import models


class RestaurantManager(models.Manager):
    def get_solo_restaurant(self):
        """
        Returns the first restaurant in the database.
        If none exists, creates a default placeholder restaurant.
        """
        restaurant = self.first()
        if not restaurant:
            restaurant = self.create(
                name="Default Restaurant",
                address="Not specified",
                phone_number="N/A"
            )
        return restaurant


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # ✅ Attach custom manager
    objects = RestaurantManager()

    def __str__(self):
        return self.name
