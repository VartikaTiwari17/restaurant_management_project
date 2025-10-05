from decimal import Decimal 


def calculate_discount(amount, percent):
      """Return discounted amount"""
      return amount - (amount * Decimal(percent) / 100)