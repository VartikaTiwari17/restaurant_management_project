from django.contrib import admin
from .models import DailyOperatingHours  # Import your model

# Register the model to make it editable in Django admin
admin.site.register(DailyOperatingHours)
