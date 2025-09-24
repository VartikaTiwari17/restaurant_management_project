from django.db import models
from .models import OrderStatus  # Make sure this import exists


class Order(models.Model):
      # your existing fields...
      status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)


      # other fields and methods...