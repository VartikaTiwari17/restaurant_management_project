from django.db.models import Avg
from home.models import MenuItem

def get_average_prep_time_by_category(category_id):
    """
    Calculate the average preparation time for all menu items
    in a specific category.
    """
    if not category_id:
        return None

    # Filter menu items by the given category_id
    menu_items = MenuItem.objects.filter(category_id=category_id)

    if not menu_items.exists():
        return None  # or return 0, depending on your preference

    # Calculate average using Django ORM aggregation
    avg_time = menu_items.aggregate(avg_prep=Avg('prep_time_minutes'))['avg_prep']

    return avg_time if avg_time is not None else 0
