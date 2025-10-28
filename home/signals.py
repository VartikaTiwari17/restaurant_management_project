from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import MenuItem

@receiver(pre_save, sender=MenuItem)
def detect_price_change(sender, instance, **kwargs):
    """Detect price changes in MenuItem and log them."""
    if not instance.pk:
        # New object, skip comparison
        return

    try:
        old_instance = MenuItem.objects.get(pk=instance.pk)
    except MenuItem.DoesNotExist:
        return

    if old_instance.price != instance.price:
        print(
            f"💰 Price change detected for '{instance.name}': "
            f"{old_instance.price} → {instance.price}"
        )
