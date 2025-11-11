from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Feedback

@receiver(post_save, sender=Feedback)
def feedback_submitted(sender, instance, created, **kwargs):
    if created:
        subject = "New Customer Feedback Received"
        message = (
            f"A new feedback has been submitted.\n\n"
            f"Name: {getattr(instance, 'name', 'N/A')}\n"
            f"Email: {instance.email}\n"
            f"Message:\n{instance.message}\n"
        )
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@restaurant.com")
        recipient_list = ['admin@restaurant.com']

        try:
            # Try to send email (works if email backend is configured)
            send_mail(subject, message, from_email, recipient_list)
            print("📩 Email sent successfully to admin!")
        except Exception as e:
            # Fallback for dev/testing
            print(f"⚠️ Feedback signal triggered, but email not sent: {e}")
            print("DEBUG MESSAGE:\n", message)
