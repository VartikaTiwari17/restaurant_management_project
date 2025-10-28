from django.contrib import admin
from .models import Order

# Custom admin action
def mark_orders_processed(modeladmin, request, queryset):
    updated = queryset.update(status='Processed')
    modeladmin.message_user(request, f"{updated} orders marked as Processed.")

mark_orders_processed.short_description = "Mark selected orders as Processed"

# Register the Order model with custom admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    list_filter = ('status',)
    actions = [mark_orders_processed]
