from django.db import models

class MenuItem(models.Model):
     name = models.CharField(max_length=100)
      price = models.DecimalField(max_digits=7, decimal_places=2)
      is_daily_special = models.BooleanField(default=False)



     def __str__(self):
        return self.name