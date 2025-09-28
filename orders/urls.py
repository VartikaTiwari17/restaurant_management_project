from django.urls import path, include
from rest_framework.routers import DeafultRouter
from .view import OrderViewSet


router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path ('api/', include(router.urls)),
]