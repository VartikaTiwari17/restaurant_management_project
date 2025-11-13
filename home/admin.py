from django.contrib import admin # type: ignore
from .models import RestaurantImage

@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'uploaded_at')
