from django.contrib.auth.models import User
from .models import LoyaltyPoint

def get_user_total_loyalty_points(user):
    """
    Returns the total loyalty points for a given user.
    If the user has no loyalty points, returns 0.
    """
    if not isinstance(user, User):
        raise ValueError("Expected a User instance.")

    total_points = LoyaltyPoint.objects.filter(user=user).aggregate(total_points_sum=models.Sum('points'))['total_points_sum']
    return total_points or 0
