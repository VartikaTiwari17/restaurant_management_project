# home/urls.py
from django.urls import path
from .views import ActiveMenuItemsListView

urlpatterns = [
    path('api/menu/active/', ActiveMenuItemsListView.as_view(), name='active-menu-items'),
]
