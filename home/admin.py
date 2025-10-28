from django.contrib import admin
from django.utils.html import format_html
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'availability_status')

    def availability_status(self, obj):
        """Display a green check if active, red cross if not."""
        if obj.is_active:
            return format_html('<span style="color: green;">✔️ Available</span>')
        return format_html('<span style="color: red;">❌ Unavailable</span>')

    availability_status.short_description = 'Availability'
