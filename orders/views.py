from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, time
from .models import Reservation

class AvailableSlotsAPIView(APIView):
    """
    API to check available reservation slots for a given date.
    Example: /api/orders/reservations/slots/?date=2025-11-15
    """

    def get(self, request):
        date_str = request.query_params.get('date')
        if not date_str:
            return Response(
                {"error": "Please provide a date in YYYY-MM-DD format."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            requested_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Define standard restaurant reservation slots
        standard_slots = [
            "18:00", "18:30", "19:00", "19:30", "20:00",
            "20:30", "21:00", "21:30", "22:00"
        ]

        # Fetch all booked times for the given date
        booked_slots = Reservation.objects.filter(date=requested_date).values_list("time", flat=True)
        booked_times = [t.strftime("%H:%M") for t in booked_slots]

        # Find available slots
        available_slots = [slot for slot in standard_slots if slot not in booked_times]

        return Response({
            "date": str(requested_date),
            "available_slots": available_slots,
        }, status=status.HTTP_200_OK)
