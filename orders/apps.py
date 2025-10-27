from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from django.db.models.signals import post_save
        from .models import Reservation, log_new_reservation

        post_save.connect(log_new_reservation, sender=Reservation)
