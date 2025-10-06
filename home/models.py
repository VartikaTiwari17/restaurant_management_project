from django.db import models
from django.contrib.auth.models import User
from .models import MenuCategory

class MenuItem(models.Model):
     name = models.CharField(max_length=100, unique=True)
     description = models.TextField(blank=True, null=True)
      def __str__(self):
        return self.name


