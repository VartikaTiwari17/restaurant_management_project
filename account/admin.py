from django.contrib import admin
from .models import LoyaltyProgram

@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'points_per_dollar', 'minimum_purchase_for_points', 'is_active')
