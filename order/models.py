from django.db import models 


class OrderStatus(models.Model):
       name = models.CharField(max_length=50, unique=True)
       user = models. DateTimeField(auto_now_add=True)



customer_notes = models.TextField(blank=True, null=True)

       def __str__(self):
          return f"Order  #{self.id} - {self.customer.username}"