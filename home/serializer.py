# home/serializer.py
from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    item_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'item_count']
