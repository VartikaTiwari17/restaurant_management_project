from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Reservation, Table

@receiver(post_save, sender=Reservation)
def update_table_on_reservation_change(sender, instance, **kwargs):
    """Automatically update table availability based on reservation status."""
    table = instance.table
    if instance.status in ['cancelled', 'completed']:
        table.is_available = True
    elif instance.status == 'confirmed':
        table.is_available = False
    table.save()
