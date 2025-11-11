from django.urls import path
from .views import DailyStatsAPIView

urlpatterns = [
    path('daily_stats/', DailyStatsAPIView.as_view(), name='daily_stats'),
]
