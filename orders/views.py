from reat_framework. views import APIView
from rest_framework. response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderStatusUpdateSerializer



class UpdateOrderStatusView(APIView):
       def put (self, request, pk):
         try:
            Order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
         return Response({"error": "Order not found"},  status=status.HTTP_404_BAD_REQUEST)
        
        
        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order status updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)


            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST})