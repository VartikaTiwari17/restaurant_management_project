from rest_framework import serializers # type: ignore
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'  # includes all fields like id, name, date, time, etc.
