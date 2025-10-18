from django.db import models
from django.contrib.auth.models import User



CUISINE_CHOICES = (
    ('Italian', 'Italian'),
     ('Mexican', 'Mexican'),
     ('Asian', 'Asian'),
     ('Vegetarian', 'Vegetarian'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delet=models.CASCADE< related_name='profile')
    preferred_cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES, blank=True, null=True)


    def __str__(self):
        return f'{self.user.username}'s Profile"