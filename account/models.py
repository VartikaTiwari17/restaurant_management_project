from django.db import models
from django.conf import settings

class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def get_full_name(self):
        """
        Returns the user's full name by combining first_name and last_name.
        Handles missing values gracefully.
        """
        first = getattr(self.user, 'first_name', '') or ''
        last = getattr(self.user, 'last_name', '') or ''
        full_name = f"{first} {last}".strip()
        return full_name or "Anonymous"

    def __str__(self):
        return self.get_full_name()
