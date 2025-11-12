from account import models


class Table(models.Model):
    name = models.CharField(max_length=50)
    # ✅ New field for maximum guests
    max_capacity = models.PositiveIntegerField(default=4, help_text="Maximum number of guests for this table")

    def __str__(self):
        return self.name
