from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=Trye, null=True)
    capacity = models.IntegerField(default=0, blank=True, null=True)
     



     def __str__(self):
        return self.name