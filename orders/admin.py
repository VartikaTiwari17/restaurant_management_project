from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'customer', 'total_amount', 'order_status')
    # Optional: add search and filtering later if needed
    # search_fields = ('customer__username', 'id')
    # list_filter = ('order_status',)

# Register the model with custom admin
admin.site.register(Order, OrderAdmin)

