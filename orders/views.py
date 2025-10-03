from reat_framework. views import APIView
from rest_framework. response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon


class CouponVaildationView(APIView):
       def post (self, request):
          code = request.data.get("code")  # User se coupon code le raha hai

            if not code:
                return Response({"error": "Coupon code is required"}, status=status.HTTP_404_BAD_REQUEST)

          try:
            coupon = Coupon.objects.get(code=code, is_active=True)
    except Coupon.DoesNotExist:
         return Response({"error": "Invalid coupon code"},  status=status.HTTP_404_BAD_REQUEST)
        
        
        today = timezone.now().date()
        if coupon.valid_form <= today <= coupon.valid_untill:
             return Response({
                "success": True,
                "discount_percentage": str(coupon.discount_percentage)
             }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Coupon is expired or not valid today."})