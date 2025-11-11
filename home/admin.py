from django.contrib import admin
from .models import DietaryTag, MenuItem

@admin.register(DietaryTag)
class DietaryTagAdmin(admin.ModelAdmin):
    list_display = ('name',)

# If MenuItem not already registered, register it
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    filter_horizontal = ('dietary_tags',)
