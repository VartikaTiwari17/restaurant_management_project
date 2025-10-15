from rest_framework import viewsets
from rest_framework.response import Response
from .models import MenuCategory
from .serializers import MenuCategorySerializer


class MenuCategoryViewSet(viewset.ViewSet):
    def list(self, request):
    categories = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer(categories, many=True)
    return Response(serializer.data)

