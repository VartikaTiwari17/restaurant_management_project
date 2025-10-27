from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OrderItem

class UpdateOrderItemQuantityView(APIView):
    def patch(self, request, pk):
        try:
            order_item = OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return Response({"error": "Order item not found."}, status=status.HTTP_404_NOT_FOUND)

        new_quantity = request.data.get("quantity")

        # Validation
        if new_quantity is None:
            return Response({"error": "Quantity is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_quantity = int(new_quantity)
        except ValueError:
            return Response({"error": "Quantity must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        if new_quantity < 0:
            return Response({"error": "Quantity must be positive."}, status=status.HTTP_400_BAD_REQUEST)

        if new_quantity == 0:
            order_item.delete()
            return Response({"message": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)

        order_item.quantity = new_quantity
        order_item.save()
        return Response({"message": "Quantity updated successfully."}, status=status.HTTP_200_OK)
