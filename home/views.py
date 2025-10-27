# home/views.py
from rest_framework import generics
from django.db.models import Count
from .models import MenuCategory
from .serializer import MenuCategorySerializer

class MenuCategoryWithCountView(generics.ListAPIView):
    """List all menu categories with the total number of items in each."""
    serializer_class = MenuCategorySerializer

    def get_queryset(self):
        return MenuCategory.objects.annotate(item_count=Count('menuitem'))
