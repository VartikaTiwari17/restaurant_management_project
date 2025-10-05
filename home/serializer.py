from rest_framework import serializers
from .models import MenuItem


class DailyspecialSerializer(serializers.ModelSerializer):
      class Meta:
         model = MenuItem
         fields = ['id', 'name', 'price']
         