from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from datetime import datetime

@receiver(user_login_failed)
def log_failed_login(sender, credentials, **kwargs):
    username = credentials.get('username', 'Unknown user')
    print(f"🚨 Failed login attempt for user: {username} at {datetime.now()}")
