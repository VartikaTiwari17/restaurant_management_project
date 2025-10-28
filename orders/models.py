from django.db import models

class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=50, unique=True)
    points_required = models.IntegerField(unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.discount_percentage}% discount)"
