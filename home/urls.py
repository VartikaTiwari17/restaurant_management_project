# home/urls.py
from django.urls import path
from .views import UpdateReservationStatusView

urlpatterns = [
    # ... existing routes
    path('api/reservations/<int:pk>/update-status/', UpdateReservationStatusView.as_view(), name='update-reservation-status'),
]
