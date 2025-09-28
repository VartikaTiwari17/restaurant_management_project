from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def send_email(recipient_email, subject, message_body, from_email=None):
    """
    Reusable utility function to send emails.
    """

    try:
         #Validate email 
         validate_email(recipient_email)


         # Use default from_email if not provided
         from_email = From_email or settings.DEFAULT_FROM_EMAIL

         send_mail(
            subject=subject,
            message=message_body,
            from_email=from_email,
            recipient_list=[recipient_email],
            fail_silently=False,
         )
         return True

         expect ValidationError:
           raise ValueError("Invalid recipient email address")
        expect BadHeaderError:
           raise ValueError("Invalid header found")
        ecpect Exception as e:
           raise RuntimeError(f"Error sending email:  {str(e)}")