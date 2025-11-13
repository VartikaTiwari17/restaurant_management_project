from django.contrib import admin # type: ignore
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_vegetarian', 'preparation_time_minutes')
