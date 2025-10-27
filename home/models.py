from django.db import models

class Allergen(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Make sure your MenuItem model looks something like this:
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    # add this line below:
    allergens = models.ManyToManyField(Allergen, blank=True)

    def __str__(self):
        return self.name
