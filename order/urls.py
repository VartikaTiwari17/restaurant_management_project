from django.urls import path
from .view import OrderHistoryView


urlpatterns = [
      path("history/", OrderHistoryView.as_view(), name="order-history"),
]