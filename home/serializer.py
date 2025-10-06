from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializer.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
         