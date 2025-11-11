from django.db import models

class RestaurantSettings(models.Model):
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=15.00)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    default_currency_symbol = models.CharField(max_length=5, default="$")

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if RestaurantSettings.objects.exists() and not self.pk:
            RestaurantSettings.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Restaurant Settings ({self.default_currency_symbol})"
