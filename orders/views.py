from django.db.models import Sum
from django.utils.dateparse import parse_date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order


class DailyStatsAPIView(APIView):
    """
    API endpoint to get total number of orders and total revenue for a specific date.
    Example: /api/orders/daily_stats/?date=2025-11-11
    """

    def get(self, request, *args, **kwargs):
        # Get date from query parameters
        date_str = request.query_params.get('date')
        if not date_str:
            return Response({'error': 'Please provide a date in YYYY-MM-DD format.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            target_date = parse_date(date_str)
            if not target_date:
                raise ValueError
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Filter orders for the given date
        orders = Order.objects.filter(created_at__date=target_date)

        # Calculate total orders and total revenue
        total_orders = orders.count()
        total_revenue = orders.aggregate(total=Sum('total_amount'))['total'] or 0

        # Return response
        data = {
            'date': date_str,
            'total_orders': total_orders,
            'total_revenue': float(total_revenue),
        }
        return Response(data, status=status.HTTP_200_OK)
