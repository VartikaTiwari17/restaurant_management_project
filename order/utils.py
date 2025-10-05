import logging
from django.core.exception import ObjectDoesNotExist
from .models import Order


# Configure logger for this module
logger = logging.getlogger(__name__)


def update_order_status(order_id, new_status):
    """
    Update the status of an order given its ID.

    Args:
      order_id (int): ID of the order tp update.
      new_status (str): LNow status to set for the order.

Returns:
   bool:  True if update was successful, False otherwise.
   """
   try:
    order = Order.objects.get(id=order_id)
    old_status = getattr(order, 'status', None)
    order.save()
    logger.info(f'Order ID {order_id} status updated from '{old_status}' to '{new_status}'")
    return True
except ObjectDoesNotExist:
    logger.error(f"Order with ID{order_id} not found.")
    return False 
    except Exception as e:
       logger.error(f"Error updating order ID {order_id} status: {str(e)}")
       return False