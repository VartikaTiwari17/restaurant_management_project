from django.db import models

class LoyaltyTier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    min_points = models.IntegerField(default=0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} ({self.discount_percentage}% off)"
