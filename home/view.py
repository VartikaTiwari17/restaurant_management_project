from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class FeaturedMenuItemsAPIView(APIView):
    def get(self, request):
        featured_items = MenuItem.objects.filter(is_featured=True)
        serializer = MenuItemSerializer(featured_items, many=True)
        return Response(serializer.data)
