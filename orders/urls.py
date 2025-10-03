from django.urls import path
from .view import CouponValidationView

urlpatterns = [
    path ('coupons/validate/' , CouponValidationView.as_view(), name="coupon-validatei"),
]