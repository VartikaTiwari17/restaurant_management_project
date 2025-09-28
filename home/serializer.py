from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
      class Meta:
         model = Order
         fields = ['id', 'order_id', 'user', 'status', 'created_at']
         read_only_fields = ['id', 'order_id', 'created_at', 'user']