from django.contrib import admin
from account.models import LoyaltyProgram

@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'points_per_dollar_spent', 'is_active', 'created_at']
    search_fields = ['name']
    list_filter = ['is_active']
