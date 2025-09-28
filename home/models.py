from django.db import models
from decimal import Decimal



class MenuItem(models.Model):
     name = models.CharField(max_length=255)
     description  = models.TextField(blank=True)
     price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))



     def __str__(self):
        return self.name