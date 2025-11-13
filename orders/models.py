from django.db import models # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from home.models import MenuItem  # assuming MenuItem is in the home app
from django.contrib.auth.models import User # type: ignore


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity})"

    # ✅ Validation method for quantity
    def clean_quantity(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be a positive number.")
        if self.quantity > 99:
            raise ValidationError("Quantity cannot exceed 99.")
