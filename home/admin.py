from django.contrib import admin
from .models import MenuItem

# ✅ Define the custom action function
def make_inactive(modeladmin, request, queryset):
    updated_count = queryset.update(is_active=False)
    modeladmin.message_user(
        request,
        f"{updated_count} menu item(s) were successfully marked as inactive."
    )

# ✅ Register MenuItem in admin with custom action
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'is_vegetarian', 'stock_quantity', 'last_modified')
    list_filter = ('is_active', 'is_vegetarian')
    actions = [make_inactive]  # ← add the custom action here
