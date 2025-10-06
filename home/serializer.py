from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializer.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name, 'price', 'is_available']
         