def calculate_estimated_prep_time(order_items):
    """
    Calculate total estimated preparation time for a list of order items.

    Args:
        order_items (list of dict): Each dict contains 'menu_item_id', 'quantity', 'prep_time_minutes'

    Returns:
        int: Total estimated prep time in minutes
    """
    total_time = 0
    for item in order_items:
        total_time += item.get('prep_time_minutes', 0) * item.get('quantity', 1)
    return total_time
