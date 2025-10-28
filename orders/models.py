class Order(models.Model):
    # existing fields (like customer, status, total, etc.)

    def get_unique_item_names(self):
        """
        Returns a list of unique menu item names associated with this order.
        """
        # Collect item names from related OrderItems
        item_names = {item.menu_item.name for item in self.orderitem_set.all()}
        return list(item_names)
