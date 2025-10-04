from rest_framework import generics
from . models import Table
from .serializers import TableSerializer




class AvailableTablesAPIView(generics.ListAPIView):
    serializer_class = TableSerializer


    def get_queryset(self):
        return Table.objects.filter(is_available=True)


class TableDetailAPIView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
