# home/serializer.py
from rest_framework import serializers
from .models import HolidayHours

class HolidayHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayHours
        fields = '__all__'
