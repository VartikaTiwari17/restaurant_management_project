from django.db import models
from django.conf import settings  # ✅ for referencing AUTH_USER_MODEL

class Feedback(models.Model):
    user = models.ForeignKey(  # 🆕 added field
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='feedbacks',
        help_text='User who submitted the feedback (optional)'
    )
    message = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_name = self.user.username if self.user else "Guest"
        return f"Feedback by {user_name} on {self.created_at.strftime('%Y-%m-%d')}"
