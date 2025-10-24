from django.db import models
from django.utils import timezone



class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)


          def __str__(self):
           return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class DailySpecial(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delte=models.CASCADE)
    date = models.DateField()

    

    cuisine = models.ForeiKey(
        Cuisine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='menu_items'
    )


    def __str__(self):
        return self.name

    