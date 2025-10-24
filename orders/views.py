from reat_framework. views import api_view
from rest_framework. response import Response
from rest_framework import status
from .models import Order


@api_view(['GET'])
def get_order_status(request, order_id):
     """
     Retrieve the current status of an order by its ID.
     """

     try:
        order = Order.objects.get(id=order_id)
        return Response({
            "order_id": order.id,
            "status": getattr(order, 'status', 'pending')
        }, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
           return Response(
                 {"error": f"Order with ID {order_id} not found."},
                 status=status.HTTP_404_NOT_FOUND
                 )

                 class TableListView(generics.ListAPIView):

                    queryset = Table.objects.all()
                    serializer_class = TableSerializer