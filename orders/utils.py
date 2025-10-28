def calculate_tip_amount(order_total, tip_percentage):
    """
    Calculates the tip amount for a given order total and tip percentage.

    Parameters:
        order_total (float or Decimal): The total bill amount before tip.
        tip_percentage (int or float): The tip percentage (e.g., 10 for 10%).

    Returns:
        float: The calculated tip amount rounded to two decimal places.
    """
    if order_total is None or tip_percentage is None:
        return 0.0

    tip_amount = order_total * (tip_percentage / 100)
    return round(tip_amount, 2)
