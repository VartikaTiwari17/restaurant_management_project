from django.contrib import admin
from .models import RestaurantSettings

@admin.register(RestaurantSettings)
class RestaurantSettingsAdmin(admin.ModelAdmin):
    list_display = ('min_order_value', 'delivery_fee', 'default_currency_symbol')
