from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender='orders.Reservation')
def log_new_reservation(sender, instance, created, **kwargs):
    if created:
        print(f"New reservation created: ID #{instance.id} for {instance.customer_name} at {instance.time}")
