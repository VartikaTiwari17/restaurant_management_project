from django.urls import path
from .view import get_order_status

urlpatterns = [
    path ('api/<order>/history/' , get_order_status, name="get-order-status"),
]