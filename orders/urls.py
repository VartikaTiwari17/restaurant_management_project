from django.urls import path
from .views import UpdateOrderItemQuantityView

urlpatterns = [
    path('order-items/<int:pk>/update-quantity/', UpdateOrderItemQuantityView.as_view(), name='update-order-item-quantity'),
]
