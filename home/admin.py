from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import DailySpecial
@admin.register(DailySpecial)
class DailySpecialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    list_filter = ('is_active',)
