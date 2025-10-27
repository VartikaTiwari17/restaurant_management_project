from django.urls import path
from .views import StaffListAPIView

urlpatterns = [
    path('api/staff/', StaffListAPIView.as_view(), name='staff-list'),
]
