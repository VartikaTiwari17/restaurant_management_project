from rest_framework import serializers
from .models  import Order


class OrderStatusUpdateSerializer(serializer.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'