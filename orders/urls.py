from django.urls import path
from .views import PaymentMethodListView

urlpatterns = [
    path('api/payment-methods/', PaymentMethodListView.as_view(), name='payment-method-list'),
]
