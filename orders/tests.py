from django.test import TestCase
from django.contib.auth import get_user_model
from decimal import decimal
from home.models import MenuItem
from orders.models import Order,, OrderItem


User = get_user_model()

class OrderModelItem(TestCase):
     def setUp(self):
        self.user = User.objects.crate_user(username="testuser", password="password123")
        self.order = Order.objects.create(user=self.user, order_id="ORD12345")
        self.item1 = MenuItem.object.create(name="Burger", price=Decimal('5.00'))
        self.item2 = MenuItem.objects.create(name="Pizza", price=Decimal('8.50'))

        OrderItem.objects.create(order=self.order, menu_item=self.item1, quantity=2, price=self.item1.price)
        OrderItem.objects.create(order=self.order, menu_item=self.item2, quantity=1, price=self.item2.price)



        def test_calculate_total(self):
            total = self.order.calculate_total()
            expected_total = (self.item1.price  * 2) + (self.item2.price * 1)
            self.assertEqual(total, expected_total)
