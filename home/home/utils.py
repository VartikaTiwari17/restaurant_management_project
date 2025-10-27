# home/utils.py
from decimal import Decimal, ROUND_HALF_UP

def format_price(value, currency_symbol='$'):
    """
    Format a numeric price value into a consistent currency format.
    Example: 15.5 -> '$15.50'
    """
    if not isinstance(value, Decimal):
        value = Decimal(str(value))
    
    # Round to 2 decimal places using standard rounding
    formatted_value = value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return f"{currency_symbol}{formatted_value:.2f}"
