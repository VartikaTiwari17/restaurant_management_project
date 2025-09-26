from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer



class MenuItemPagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50



class MenuItemsByCategoryView(viewsets. ViewSet):
 permission_classes = [permissions.AllowAny]  # open for all


      def get (self, request):
        query = request.query_params.get("search", None)
        items = MenuItem.objects.all()
        if query:
             items = item.filter(name__icontains=query)
             

        paginator = MenuItemPagination()
        paginated_items = paginator.paginate_queryset(items, request)
        serializer = MenuItemSerializer(paginated_items, many=True)
        return paginator.get_paginated_response(serializer.data)