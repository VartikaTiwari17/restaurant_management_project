from django.urls import path
from .view import UpdateOrderStatusView

urlpatterns = [
    path (update-order-status/' , UpdateOrderStatusView.as_view(), name="update_order_status"),
]