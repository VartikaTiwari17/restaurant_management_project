from django.db import  models
from djngo.contrib.auth.models import User



class Order(models.Model):
    STATUS_CHOICES =[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
    ]



    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
      def __str__(self):
        return f"Order #{self.id} - {self.user.username}  ({self.status})"


    
        