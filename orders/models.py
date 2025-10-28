class Order(models.Model):
    STATUS_PENDING = 'PENDING'
    STATUS_PROCESSED = 'PROCESSED'
    STATUS_COMPLETED = 'COMPLETED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PROCESSED, 'Processed'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    # 🆕 New method to mark order as completed
    def mark_as_completed(self):
        """Mark this order as completed and save the change."""
        self.status = self.STATUS_COMPLETED
        self.save()
