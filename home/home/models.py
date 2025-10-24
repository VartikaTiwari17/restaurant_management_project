from django.db import models 
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    is_featured = models.DecimalField(max_digits=6, decimal_places=2)
     



     def __str__(self):
        return self.name


class UserReviewa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.user.username} - {self.menu_item.name}  ({self.rating}/5)'