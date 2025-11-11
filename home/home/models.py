from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # New rating field
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True,
        help_text="Rate from 1 (worst) to 5 (best)"
    )

    def __str__(self):
        return f"{self.subject} - Rating: {self.rating if self.rating else 'N/A'}"
