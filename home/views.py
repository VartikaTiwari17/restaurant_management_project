# home/views.py
from rest_framework import generics
from .models import HolidayHours
from .serializer import HolidayHoursSerializer

class HolidayHoursListView(generics.ListAPIView):
    """API endpoint to list all holiday hours, with optional date filtering."""
    serializer_class = HolidayHoursSerializer

    def get_queryset(self):
        queryset = HolidayHours.objects.all()
        date = self.request.query_params.get('date', None)
        if date:
            queryset = queryset.filter(date=date)
        return queryset
