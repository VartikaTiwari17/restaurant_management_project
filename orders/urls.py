from django.urls import path
from .views import  OrderDetailView


urlpatterns = [
    path ('<int:id>/', OrderDetailView.as_view(), name='order-detail'),
]