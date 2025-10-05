from rest_framework import serializers
from .models  import Order


class OrderStatusUpdateSerializer(serializer.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']


        def validate_status(self, value):
            allowed_statuses = ['pending', 'processing', 'completed']
            if value not in allowed_statuses:
                raise serializers.ValidationError(f"Invalid status. Allowed values are:  {', '.join(allowed_statuses)}.")
                return value