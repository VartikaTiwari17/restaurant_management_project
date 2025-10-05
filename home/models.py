from django.db import models
from django.contrib.auth.models import User
from .models import MenuCategory

class MenuItem(models.Model):
     name = models.CharField(max_length=100)
     category = models .ForeignKey(MenuCategpory, on_delete=models.CASCADE)
     price = models.DecimalField(max_digits=6, decimal_places=2)
     description = models.TextField(blank=True, null=True)
      def __str__(self):
        return self.name


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    menu_item = model.ForeignKey('MenuItem', on_delete=models.CASCADE, related_name="reviews")
    rating= = models.IntegerField()
    comment = models.TextField()
    review_date = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.menu_item.name}"