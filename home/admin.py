from django.contrib import admin
from .models import Restaurant


 @admin.register(Table)
class Restaurant Admin(admin.ModelAdmin):
    list_display = ('name''address', 'phone_number','email', 'is_acitve')
    list_filter = ('is_active')
    search_fields = ('name', 'address')
