from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from account.models import LoyaltyPoint

@receiver(post_save, sender=Order)
def award_loyalty_points_on_order(sender, instance, created, **kwargs):
    """
    Automatically award loyalty points when a new order is created.
    """
    if created:  # Only for newly created orders
        user = instance.user
        # Find or create loyalty record for this user
        loyalty, _ = LoyaltyPoint.objects.get_or_create(user=user)
        loyalty.points += 50  # Add fixed 50 points
        loyalty.save()
