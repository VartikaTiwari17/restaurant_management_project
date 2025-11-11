from rest_framework import serializers
from .models import DailySpecial

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySpecial
        fields = ['title', 'description', 'price']  # adjust according to your model fields
