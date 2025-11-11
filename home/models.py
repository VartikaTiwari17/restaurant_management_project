from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(default=0, help_text="Current available stock of this item")
    last_modified = models.DateTimeField(auto_now=True)  # ✅ Automatically updates on save

    def __str__(self):
        return self.name
