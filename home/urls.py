from django.urls import path
from .views import DailySpecialListView

urlpatterns = [
    path('api/daily-specials/', DailySpecialListView.as_view(), name='daily-special-list'),
]
