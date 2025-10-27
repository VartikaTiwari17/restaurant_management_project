from django.db import models
from django.utils import timezone

# Assuming you already have RestaurantStaff model somewhere above
class RestaurantStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class StaffShift(models.Model):
    staff_member = models.ForeignKey(RestaurantStaff, on_delete=models.CASCADE, related_name="shifts")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.staff_member.name} - {self.date} ({self.start_time} to {self.end_time})"
