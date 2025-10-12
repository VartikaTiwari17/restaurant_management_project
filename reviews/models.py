from django.db import models
from home.models import Restaurant
from django.contrib.auth.models import User


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models,CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name}"