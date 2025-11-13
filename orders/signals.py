from django.db.models.signals import post_delete # type: ignore
from django.dispatch import receiver # type: ignore
from orders.models import OrderItem
from home.models import MenuItem  # assuming MenuItem model has stock_quantity field


@receiver(post_delete, sender=OrderItem)
def update_inventory_on_order_item_delete(sender, instance, **kwargs):
    """
    When an OrderItem is deleted, restore its quantity to the MenuItem's stock.
    """
    menu_item = instance.menu_item
    if hasattr(menu_item, 'stock_quantity'):  # Ensure field exists
        menu_item.stock_quantity += instance.quantity
        menu_item.save()
