from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('draft', 'Draft'),
        ('in_cart', 'In Cart'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ New method to check if order can still be modified
    def is_editable(self):
        """
        Returns True if the order can still be modified.
        Orders in 'pending', 'draft', or 'in_cart' states are editable.
        """
        editable_statuses = ['pending', 'draft', 'in_cart']
        return self.status in editable_statuses

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
