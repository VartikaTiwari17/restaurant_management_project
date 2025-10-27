from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'contact_email')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)
