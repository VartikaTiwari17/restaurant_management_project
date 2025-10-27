from django.db import models

class FeedbackCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    # existing fields (example — replace or keep as your original ones)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # new category field
    category = models.ForeignKey(
        FeedbackCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='feedbacks'
    )

    def __str__(self):
        return f"{self.name} - {self.category.name if self.category else 'No Category'}"
