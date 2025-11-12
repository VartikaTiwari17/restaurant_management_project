from django.contrib import admin
from .models import RestaurantAnnouncement

@admin.register(RestaurantAnnouncement)
class RestaurantAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'is_active')
    list_filter = ('is_active', 'publish_date')
    search_fields = ('title', 'content')
