from rest_framework import generics
from .models import DailySpecial
from .serializers import DailySpecialSerializer

class DailySpecialListView(generics.ListAPIView):
    queryset = DailySpecial.objects.all()
    serializer_class = DailySpecialSerializer
