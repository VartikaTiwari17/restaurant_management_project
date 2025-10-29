class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    calories = models.IntegerField(null=True, blank=True)
    is_gluten_free = models.BooleanField(default=False)

    # Attach custom manager
    objects = MenuItemManager()

    def __str__(self):
        return self.name
