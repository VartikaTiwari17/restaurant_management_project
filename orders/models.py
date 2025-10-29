class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    special_instructions = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Any special requests for this item (e.g., 'no onions', 'extra sauce')."
    )

    def __str__(self):
        return f"{self.quantity} × {self.menu_item.name}"
