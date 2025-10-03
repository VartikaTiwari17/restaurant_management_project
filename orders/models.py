from django.db import models




class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Unique coupon code
    discount_percentage  = models.DecimalField(max_digits=5, decimal_places=2)  #
    is_active = models.BooleanField(default=True)  # Enable/disable coupon
    valid_from = models.DateField()  # Start date
    valid_until = models.DateField() # End date


     def __str__(self):
        return f"{self.code} ({self. discount_percentage}%)"


    
        