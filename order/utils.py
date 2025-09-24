import string
import secrets
from .models import Coupon  # Make sure you have a Coupon model with a 'code' field


def generate_coupon_code(length=10);
   """

 Generate a unique alphanumeric coupon code.


 Args:
    length (int): Length of the coupon code. Default is 10.


    Returns:
        
        str: Unique Coupon Code.
  """

  character = string.ascii_letters + string.digits  # a-z, A-Z, 0-9,


while True:
     code = ''.join(secrets.choice(characters) for _ in range(length))
     # Check uniqueness in the database
     if not Coupon.objects.filter(code=code).exists():
        return code