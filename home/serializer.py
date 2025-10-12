from rest_framework import serializers
from .models import MenuCategory


class MenuCategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', name','description','price', 'image' 'is_available']   # Only essential details
         