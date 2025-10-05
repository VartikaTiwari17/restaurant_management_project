from reat_framework. views import APIView
from rest_framework. response import Response
from rest_framework import status
from .models import Order



class UpdateOrderStatusView(APIView):
       def put (self, request):
         order_id = request.data.get('order_id')
         new_status = request.data.get('new_status')


        # Validate presence of both fields
        if not order_id or not new_status:
            return Response(
                {"error": "Both 'order_id' and 'new_staus' are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
              # Validate allowed statuses
              allowed_statuses = ['Pending', 'Processing', 'Delivered']
              if new_status not in allowed_statuses:

                return Response(
                    {"error": f"Invalid staus. Allowed values are:  {', '.join(allowed_statuses)}."},
                    status=status.HTTP_400_BAD_REQUEST
                )


                # Check if order exists
                try:
                    order = Order.objects.get(id=order_id)
                 except Order.DoesNotExist:
                    return Response(
                        {"error": "Order not found"},
                        status=status.HTTP_400_BAD_FOUND
                    )


                    # Update status
                    order .status = new_status
                    order.save()


            return Response(
                 {"message": "Order status updated successfully.", "order_id": order.id,  "new_status": order.status},
                 status=status.HTTP_200_OK