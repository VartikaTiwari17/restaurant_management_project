from django.urls import path
from home.views import RestaurantDetailView

urlpatterns = [
    path('api/restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
]
