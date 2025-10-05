from django.urls import path
from .view import daily_specials


urlpatterns = [
    path('api/daily-specials/', daily_specials,  name='daily_specials'),

]