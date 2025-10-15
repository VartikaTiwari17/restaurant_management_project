from django.db import  models
from djngo.contrib.auth.models import User



class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('DELIVERIED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]


    
    user = models ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')


    def __str__(self):
        return f"Order  #{self.id} by {self.status}"





    
        