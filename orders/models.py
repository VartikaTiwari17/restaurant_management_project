from django.db import models
from home.models import MenuItem

class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"
