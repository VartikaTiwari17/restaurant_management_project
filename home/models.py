class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    calories = models.IntegerField(null=True, blank=True)  # ✅ new optional field

    def __str__(self):
        return self.name
