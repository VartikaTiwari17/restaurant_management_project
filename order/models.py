from django.db import models


class OrderStatus(models.Model):
     name = model.CharField(max_length=50, unique=True)

       def __str__(self):
        return self.name