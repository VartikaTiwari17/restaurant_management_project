from django.db import models


class MenuItem(models.Model):
     name = models.CharField(max_length=100)
     address = models.TextField()
     phone_number = models.CharField(max_length=15)
     opening_hours = models.CharField(max_length=100)
     email = models.EmailField(blank=True, null=True)
     website = models.URLField(blank=True, nill=True)
     description = models.TextField(blank=True, null=True)
     
     
      def __str__(self):
        return self.name


