def check_dietary_compliance(menu_item, dietary_preferences):
    """
    Checks if a given menu_item meets the specified dietary preferences.
    
    Args:
        menu_item: MenuItem instance with boolean dietary fields.
        dietary_preferences: list of strings like ['vegan', 'gluten_free', 'vegetarian']
    
    Returns:
        bool: True if the menu item meets all preferences, False otherwise.
    """
    for preference in dietary_preferences:
        # dynamically get the boolean attribute from the model
        if not getattr(menu_item, f"is_{preference}", False):
            return False
    return True
