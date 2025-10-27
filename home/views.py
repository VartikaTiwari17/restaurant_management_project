from rest_framework import generics
from .models import StaffShift
from .serializers import StaffShiftSerializer

class StaffShiftListView(generics.ListAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
