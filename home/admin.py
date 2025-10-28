from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name',)

    # 🆕 Custom admin action
    def make_unavailable(self, request, queryset):
        queryset.update(is_available=False)
        self.message_user(request, f"{queryset.count()} menu items marked as unavailable.")

    make_unavailable.short_description = "Mark selected items as unavailable"

    actions = ['make_unavailable']
