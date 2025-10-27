from rest_framework import serializers
from .models import StaffShift

class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'
