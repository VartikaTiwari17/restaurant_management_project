from django.db import models
from django.conf import settings
from decimal import decimal
from home.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]


    user = models.ForignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at  = models.DateTimeField(auto_now_add=True)


     def __str__(self):
        return f"Order {self.order_id}- {self.status}"


    def calculate_total(self):
        total = Decimal('0.00')
        for item in self.items.all():
             total  += item.price * item.quantity
           return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PostiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))



    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order {self.order.order_id}"
        