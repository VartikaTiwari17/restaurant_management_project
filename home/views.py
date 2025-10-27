# home/views.py
from rest_framework import generics
from .models import MenuItem
from .serializer import MenuItemSerializer

class ActiveMenuItemsListView(generics.ListAPIView):
    """API endpoint to list all active menu items."""
    queryset = MenuItem.objects.filter(is_active=True)
    serializer_class = MenuItemSerializer
