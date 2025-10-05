from django.urls import path
from .view import UpdateOrderStatusView

urlpatterns = [
    path ('orders/<int:pk>/update-status/' , UpdateOrderStatusView.as_view(), name="update_order_status"),
]