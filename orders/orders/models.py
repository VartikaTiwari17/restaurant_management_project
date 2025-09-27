from django.db import models


class ActiveOrderManager(models.Manager):
      def get_active_orders(self):
         return self.filter(status_in=['pending', 'processing'])


class Order(models.Models):
     STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
     ]

     user = models.FroeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')
     status = models.CharField(max_length=20, choices=STATUS_CHOICES,  default='pending')
     total_price = models. DecimalField(max_digits=10, decimal_places=2)
     created_at = models.DateTimeField(auto_now_add=True)


     objects = ActiveOrderManager()    # Custom Manager

     def __str__(self):
          return f"Order {self.id} - {self.status}"