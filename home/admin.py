from django.contrib import admin
from .models import MenuItem, Allergen

admin.site.register(Allergen)
admin.site.register(MenuItem)
