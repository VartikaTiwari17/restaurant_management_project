from django.contrib import admin
from home.models import MenuItem
@admin.action(description='Mark selected items as available')
def make_menu_items_available(modeladmin, request, queryset):
    updated = queryset.update(is_available=True)
    modeladmin.message_user(
        request,
        f"{updated} menu item(s) marked as available."
    )

@admin.action(description='Mark selected items as unavailable')
def make_menu_items_unavailable(modeladmin, request, queryset):
    updated = queryset.update(is_available=False)
    modeladmin.message_user(
        request,
        f"{updated} menu item(s) marked as unavailable."
    )
