from django.urls import path
from .views import RestaurantStatusAPIView

urlpatterns = [
    path('api/restaurant/status/', RestaurantStatusAPIView.as_view(), name='restaurant_status'),
]
