from django.contrib import admin
from .models import LoyaltyPoint

@admin.register(LoyaltyPoint)
class LoyaltyPointAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'last_updated')
    search_fields = ('user__username',)
    list_filter = ('last_updated',)
