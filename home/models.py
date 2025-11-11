from django.db import models
from django.utils import timezone

# ✅ Step 1A: Create custom manager
class DailySpecialManager(models.Manager):
    def for_today(self):
        today = timezone.now().date()
        return self.filter(valid_on_date=today)


# ✅ Step 1B: Define or enhance the model
class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    valid_on_date = models.DateField()

    # Attach custom manager
    objects = DailySpecialManager()

    def __str__(self):
        return f"{self.name} ({self.valid_on_date})"
