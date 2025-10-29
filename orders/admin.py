touch orders/admin.py
from django.contrib import admin
from orders.models import Cuisine

@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # shows these fields in the admin list view
    search_fields = ('name',)        # optional: makes searching easier
    prepopulated_fields = {'slug': ('name',)}  # optional: auto-fill slug from name
