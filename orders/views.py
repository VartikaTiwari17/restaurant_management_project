from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer


class OrderDetailView(denerics.RetrieveAPIView):
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     permission_classes = [permissions.IsAuthenticated]
     lookup_field = 'id'
