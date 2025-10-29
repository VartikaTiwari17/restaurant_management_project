from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from .models import Order, Coupon

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_coupon(request):
    coupon_code = request.data.get('coupon_code')
    order_id = request.data.get('order_id')

    if not coupon_code or not order_id:
        return Response({"error": "Coupon code and order ID are required."},
                        status=status.HTTP_400_BAD_REQUEST)

    # Step 1: Validate coupon existence
    try:
        coupon = Coupon.objects.get(code=coupon_code)
    except Coupon.DoesNotExist:
        return Response({"error": "Invalid coupon code."}, status=status.HTTP_400_BAD_REQUEST)

    # Step 2: Check coupon validity
    if not coupon.is_active:
        return Response({"error": "This coupon is not active."}, status=status.HTTP_400_BAD_REQUEST)

    if coupon.expiration_date and coupon.expiration_date < timezone.now():
        return Response({"error": "This coupon has expired."}, status=status.HTTP_400_BAD_REQUEST)

    # Step 3: Retrieve order and ensure it belongs to current user
    try:
        order = Order.objects.get(id=order_id, user=request.user, status='pending')
    except Order.DoesNotExist:
        return Response({"error": "Order not found or not eligible for coupon."},
                        status=status.HTTP_400_BAD_REQUEST)

    # Step 4: Apply coupon
    if getattr(order, 'coupon_applied', None):
        return Response({"error": "A coupon has already been applied to this order."},
                        status=status.HTTP_400_BAD_REQUEST)

    # Calculate discount
    discount_amount = (order.total_amount * coupon.discount_percentage) / 100
    new_total = order.total_amount - discount_amount

    # Step 5: Update order
    order.coupon_applied = coupon
    order.discount_applied = discount_amount
    order.total_amount = new_total
    order.save()

    return Response({
        "message": f"Coupon '{coupon_code}' applied successfully!",
        "discount": discount_amount,
        "new_total": new_total
    }, status=status.HTTP_200_OK)
