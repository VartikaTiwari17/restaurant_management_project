from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from django.utils import timezone
from .models import FailedLoginAttempt

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    username = credentials.get('username', 'Unknown')
    ip_address = None

    if request:
        ip_address = request.META.get('REMOTE_ADDR')

    FailedLoginAttempt.objects.create(
        username=username,
        ip_address=ip_address,
        timestamp=timezone.now()
    )
