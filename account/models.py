from django.db import models
from django.contrib.auth.models import User
from home.models import MenuItem  # assuming MenuItem already exists

class FavoriteMenuItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'menu_item')  # prevent duplicate favorites

    def __str__(self):
        return f"{self.user.username} - {self.menu_item.name}"
