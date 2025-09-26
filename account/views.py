from rest_framework import viewsets, permissions, status
from rest_framework.response import response
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemViewSet(viewsets. ViewSet):
     permission_classes = [permissions.IsAdminUser]   # Only admin can update


     def update(self, request, pk=None):

        try:
            item = MenuItem.objects.get(pk=pk)
        expect MenuItem.DoesNotExist:
          return Response({"error":  "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)


          serializer = MenuItemSerializer(item, data=request.data, partial=True)
          if serializer.is_vaild():
              serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
             else:
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
