from django.db import models

class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=50, unique=True)
    points_per_dollar_spent = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
