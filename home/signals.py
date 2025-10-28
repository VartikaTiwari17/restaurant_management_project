from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import MenuCategory

@receiver(post_save, sender=MenuCategory)
def log_new_menu_category(sender, instance, created, **kwargs):
    if created:
        print(f"New Menu Category created: {instance.name}")
