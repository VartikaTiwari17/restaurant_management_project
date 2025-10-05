from django.db import models
from decimal import decimal
from .utils import calculate_discount   # assume yeh function utils.py me hai

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')


    def calculate_total(self):
        total = Decimal('0.00')
        for item in self.items.all():
            amount = Decimal(item.price) * item.quantity
            amount = calculate_discount(amount, item.discount)
            total += amount
        return round(total, 2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on+on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)