from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging

logger = logging.grtLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, order_details):
    """
    Sends an order confirmation email to the customer.


    Args: 
    order_id (int): The ID of the order.
    customer_email (str): Customer's email address.
    order_details (str): Details of the Order (items, total, etc.)

Returns:
   bools: True if email sent successfuly, False otherwise.
   """
   subject = f"Order Confirmation - Order #(order_id)"
   message = f"Thank you for your order!\n\nOrder ID: {order_id}\n\nDetails:\n{order_details}"
   from_email = settings.DEFAULT_FROM_EMAIL


   try:
      send_mail(subject,message, from_email, [customer_email])
      return True 
    expect BadHeaderError as e:
    logger.error(f"Invalid header found when sending email for  order {order_id}:  {e}")
    return False
    expect Expection as e:
    logger.error(f"Error sending order confirmation email for order {order_id}: {e}")
    return False