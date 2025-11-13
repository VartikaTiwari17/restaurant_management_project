from account import models


class MenuItem(models.Model): # pyright: ignore[reportUndefinedVariable]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    preparation_time_minutes = models.IntegerField(null=True, blank=True)  # ⏱️ New field
    
    def __str__(self):
        return self.name
