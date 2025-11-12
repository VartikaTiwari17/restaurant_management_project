from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .models import DailyOperatingHours, HolidayHours

class RestaurantStatusAPIView(APIView):
    def get(self, request, *args, **kwargs):
        current_datetime = datetime.now()
        current_day = current_datetime.strftime("%A").lower()  # e.g., 'monday'

        # Check if today is a holiday
        holiday = HolidayHours.objects.filter(date=current_datetime.date()).first()
        if holiday:
            return Response({"is_open": False, "message": "Restaurant is closed today due to a holiday."})

        # Get today’s operating hours
        hours = DailyOperatingHours.objects.filter(day=current_day).first()
        if not hours:
            return Response({"is_open": False, "message": "Operating hours not found."})

        # Check if restaurant is currently open
        if hours.opening_time <= current_datetime.time() <= hours.closing_time:
            return Response({"is_open": True, "message": "Restaurant is open!"})
        else:
            return Response({"is_open": False, "message": "Restaurant is currently closed."})
