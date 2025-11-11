from django.contrib import admin
from .models import DailySpecial

@admin.register(DailySpecial)
class DailySpecialAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_on_date')
    list_filter = ('valid_on_date',)
