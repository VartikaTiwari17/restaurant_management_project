from django.db import models
from decimal import decimal


from .models import Order 
from home.models import MenuItem 


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )


    menu_item = models. ForeifnKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    

    quantity = models.IntegerField(default=1)
    price_at_time_of_order = models. DecimalField(
        max_digits=10,
        decimal_places=2
    )


    def __str__(self):
        return f'{self.quantity} * {self.menu_item.name}'