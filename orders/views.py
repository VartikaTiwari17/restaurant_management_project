from reat_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework. response import response
from django.shortcuts import get_objects_or_404
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
      queryset = Order.object.all()
      serializer_class = OrderSerializer

      @action(detail=True, methods=['delete'], url_path='cancel')
      def cancel_order(self, request, pk=None):
          order = get_object_or_404(Order, pk=pk)


          #Ensure user owns the order
          if order.usr  != request.user:
              return Response(
                {"error": "You do not have permission to cancel this order."},
                status=status.HTTP_403_FORBIDDEN
              )
              if order.status =='CANCELLED':
                   return Response(
                    {"message": "Order is already canceelled."},
                    status=status.HTTP_404_BAD_REQUEST
                   )

                   #update status
                   order.status = 'CANCELLED'
                   order.save()


                   return Response(
                    {"message": f"Order {order.order_id} has been cancelled."},
                    status=status.HTTP_200_OK
                   )