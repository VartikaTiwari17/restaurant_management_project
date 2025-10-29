from django.db import models

class FailedLoginAttempt(models.Model):
    username = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.timestamp} ({self.ip_address})"
