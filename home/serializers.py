from rest_framework import serializers
from home.models import Restaurant, DailyOperatingHours

class DailyOperatingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyOperatingHours
        fields = ['day_of_week', 'open_time', 'close_time']


class RestaurantSerializer(serializers.ModelSerializer):
    operating_hours = DailyOperatingHoursSerializer(many=True, read_only=True, source='dailyoperatinghours_set')

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'contact_number', 'email', 'has_delivery', 'operating_hours']
