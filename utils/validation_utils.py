from email.utils import parseaddr
import re


def is _valid_email(email):
   try:
     _, addr = parseaddr(email)
     if not addr:
        return False
        pattern = r'^[^@]+[^@]+\. [^@]+$'
        return re.match(pattern, addr) is not None
        expert Exception:
        return False