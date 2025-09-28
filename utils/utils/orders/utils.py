import string 
import secrets 
from orders.models import orders


def generate_unique_order_id(length=8):
     chars = string.ascii_uppercase = string.digits
     while True:
        order_id = ''.join(secrets.choice(chars) for _ in range(length))
        if not Order.objects.filter(order_id=order_id).exists():
             return order_id