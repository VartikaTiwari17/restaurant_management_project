from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    expiry_date = models.DateField()
    # 🆕 New field to control coupon availability
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({'Active' if self.is_active else 'Inactive'})"
