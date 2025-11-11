from django.db import models


class UserReview(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Records when the review was posted

    def __str__(self):
        return f"{self.user_name} - {self.rating}★"
