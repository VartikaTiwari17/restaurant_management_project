from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import FavoriteMenuItem
from home.models import MenuItem
from .serializers import FavoriteMenuItemSerializer

class AddFavoriteMenuItemAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        menu_item_id = request.data.get('menu_item_id')

        if not menu_item_id:
            return Response({'error': 'menu_item_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
        except MenuItem.DoesNotExist:
            return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check for existing favorite
        if FavoriteMenuItem.objects.filter(user=request.user, menu_item=menu_item).exists():
            return Response({'error': 'Already added to favorites'}, status=status.HTTP_400_BAD_REQUEST)

        favorite = FavoriteMenuItem.objects.create(user=request.user, menu_item=menu_item)
        serializer = FavoriteMenuItemSerializer(favorite)

        return Response({'message': 'Added to favorites', 'data': serializer.data}, status=status.HTTP_201_CREATED)
