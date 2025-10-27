# home/serializer.py
from rest_framework import serializers
from .models import Reservation

class ReservationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['status']
