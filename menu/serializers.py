from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
     class Meta:
        model = MenuItem
        fields = ["id", "name","description", "price", "available", "category"]


        def validate_price(self, value):
             if value < 0:

                raise serializers.ValidationError("Price must be s positive number.")
                return value