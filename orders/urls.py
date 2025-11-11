from .views import AvailableSlotsAPIView

urlpatterns = [
    path('reservations/slots/', AvailableSlotsAPIView.as_view(), name='available_slots'),
]
