# home/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Reservation
from .serializer import ReservationStatusSerializer

class UpdateReservationStatusView(generics.UpdateAPIView):
    """API endpoint for updating reservation status"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationStatusSerializer

    def update(self, request, *args, **kwargs):
        reservation = self.get_object()
        new_status = request.data.get('status')

        allowed_statuses = [choice[0] for choice in Reservation.STATUS_CHOICES]
        if new_status not in allowed_statuses:
            return Response(
                {"error": "Invalid status. Choose from: " + ", ".join(allowed_statuses)},
                status=status.HTTP_400_BAD_REQUEST
            )

        reservation.status = new_status
        reservation.save()
        return Response({"message": f"Reservation status updated to '{new_status}'."})
