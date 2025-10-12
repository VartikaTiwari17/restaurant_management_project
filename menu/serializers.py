from rest_framework import serializers
from .models import  Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
     class Meta:
        model = OrderItem
        fields = [ 'product name','quantity' ,'price',]


    class ReviewSerializer(serializers.ModelsSerializer):
        items = OrderItemSerializer(many=True, read_only=True)



        class Meta:
            models = Ordr 
            fields = ['id', 'customer', 'total_price','status', 'created_at', 'items']