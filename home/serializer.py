from rest_framework import serializers
from .models import MenuCategory


class MenuCategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'image']   # Only essential details
         