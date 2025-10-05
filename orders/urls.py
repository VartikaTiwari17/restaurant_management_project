from django.urls import path
from .view import get_order_status

urlpatterns = [
    path ('order-status/<int:order_id>/' , get_order_status, name="get-order-status"),
]