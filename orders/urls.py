from django.urls import path
from .views import ActivePaymentMethodsListView

urlpatterns = [
    path('api/payment-methods/', ActivePaymentMethodsListView.as_view(), name='payment-methods-list'),
]
