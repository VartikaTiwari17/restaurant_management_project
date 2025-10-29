class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    calories = models.IntegerField(null=True, blank=True)
    is_gluten_free = models.BooleanField(
        default=False,
        help_text='Indicates if the menu item is gluten-free.'
    )

    def __str__(self):
        return self.name
