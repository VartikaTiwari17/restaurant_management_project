from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'name', 'email', 'phone_number', 'date', 'time', 'number_of_guests', 'notes']
