from rest_framework import generics # type: ignore
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationDetailAPIView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
