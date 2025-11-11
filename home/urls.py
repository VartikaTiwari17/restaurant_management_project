from django.urls import path
from .views import FeedbackSubmissionAPIView

urlpatterns = [
    path('feedback/submit/', FeedbackSubmissionAPIView.as_view(), name='feedback_submit'),
]
