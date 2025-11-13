from account import models


class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)  # New field

    def __str__(self):
        return self.name
