from .models import LoyaltyProgram

def calculate_loyalty_points(order):
    """
    Calculates total loyalty points for a given order.
    Points are based on active loyalty programs that the order qualifies for.
    """
    total_points = 0
    active_programs = LoyaltyProgram.objects.filter(is_active=True)

    for program in active_programs:
        if order.total_amount >= program.minimum_purchase_for_points:
            # Calculate points for this program
            points = int(order.total_amount * program.points_per_dollar)
            total_points += points

    return total_points
