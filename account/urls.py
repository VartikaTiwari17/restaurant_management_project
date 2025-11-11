from django.urls import path
from .views import MyReviewsAPIView

urlpatterns = [
    path('api/my-reviews/', MyReviewsAPIView.as_view(), name='my_reviews'),
]
