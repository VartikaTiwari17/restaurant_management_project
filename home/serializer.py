from rest_framework import Serializers
from .models import Table




class TableSerializer(serializer.ModelSerializer):
    


    class Meta:
        model = Table
        fields = ['id','table_number', 'capacity' 'is_available', 'location']   # Only essential details
         