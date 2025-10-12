def calculate_total_price(order_items):
    """
    Calculate the total price of an order.


    Args:
      order_items (list):


    Returns:
      float: Toatl price of all order items.
     """
     return round(sum(item.get('price', 0)*  item.get('quantity', 0)for item in order_items), 2)





     if __name__=="__main__":
        order_items = [
            {'price': 120.5, 'quantity': 2},
            {'price': 80, 'quantity':1},
             {'price': 45.75, 'quantity': 3}
        ]

        total = calculate_total_price(order_items)
        peint(f"Discount amount Price: {discount_amount}")
