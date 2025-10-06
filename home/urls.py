from django.urls import path
from .view import daily_restaurant_info


urlpatterns = [
    path('api/restaurant/', get_restaurant_info,  name='get_restaurant_info'),

]