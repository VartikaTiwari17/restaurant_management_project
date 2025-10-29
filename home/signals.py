touch home/signals.py
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Feedback

# Configure logger
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Feedback)
def log_new_feedback(sender, instance, created, **kwargs):
    """
    Logs a message whenever new feedback is created.
    """
    if created:
        logger.info(f"New feedback received from {instance.email}: {instance.subject}")
