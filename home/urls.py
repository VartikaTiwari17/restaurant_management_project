from django.urls import path
from .views import FeedbackStatusUpdateAPIView

urlpatterns = [
    path('api/feedback/<int:pk>/status/', FeedbackStatusUpdateAPIView.as_view(), name='feedback_status_update'),
]
