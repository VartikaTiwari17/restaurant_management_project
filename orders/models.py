from django.db import  models



# Example  OrderStatus model 
class OrderStatus(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


# Custom manager for Order 
class OrderManager(models.Manager):
    def get_orders_by_status(self, status_name):
        """
        Retrieve all orders with a specific status.
        Example: Order.objects.get_orders_by_status('pending)
        """
        return self.filter(status__name=status_name)

# Order model with custom manager
class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    # Attach the custom manager
    objects = OrderManager()


    def __str__(self):
        return f"Order #{self.id} - Status:  {self.status.name}"


    
        