from datetime import date
from django.db.models import Sun 
from .models import Order


def get_daily_sales_total(target_data: date)  -> float:
    """
    Calculate the total sales for a given date.
    :param target_date: A datetime.data object
    :return: Total sales(float/decimal).  Return 0 if no sales.
    """

    total = (
        Order.objects.filter(created_at__date=target_date)
        .aggregate(total_sum=Sum('total_price'))['total_sum']
        or 0 
    )
    return total
