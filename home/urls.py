from django.urls import path
from .views import FeedbackListView

urlpatterns = [
    path('api/feedbacks/', FeedbackListView.as_view(), name='feedback-list'),
]
