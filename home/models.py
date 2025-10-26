from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    max_capacity = models.IntegerField(null=True, blank=True)  # New field added

    def __str__(self):
        return self.name
