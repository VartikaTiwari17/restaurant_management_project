from rest_framework import Serializers
from .models import Table




class TableSerializer(serializer.ModelSerializer):
    


    class Meta:
        model = Cuisine
        fields = ['id','name']   # Only include the fields ypu want in JSON
         