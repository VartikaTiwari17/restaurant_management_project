from django.contrib import admin
from django.utils.html import format_html
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'display_featured_image_thumbnail')

    def display_featured_image_thumbnail(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />', obj.featured_image.url)
        return "No Image"

    display_featured_image_thumbnail.short_description = "Featured Image"
