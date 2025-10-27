from rest_framework import generics
from django.db.models import Count
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.annotate(item_count=Count('menuitem'))
    serializer_class = MenuCategorySerializer
