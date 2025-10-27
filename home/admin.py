from django.contrib import admin
from .models import Feedback, FeedbackCategory

admin.site.register(Feedback)
admin.site.register(FeedbackCategory)
