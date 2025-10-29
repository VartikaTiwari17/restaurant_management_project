from django.urls import path
from .views import apply_coupon

urlpatterns = [
    path('orders/apply_coupon/', apply_coupon, name='apply_coupon'),
]
