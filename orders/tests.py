from django.test import TestCase
from decimal import Decimal
from .utils import calculate_sales_tax

class UtilsTestCase(TestCase):
    def test_calculate_sales_tax(self):
        self.assertEqual(calculate_sales_tax(Decimal("100.00"), Decimal("0.05")), Decimal("5.00"))
