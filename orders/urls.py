from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('reservations/<int:pk>/', views.ReservationDetailAPIView.as_view(), name='reservation-detail'),
]
