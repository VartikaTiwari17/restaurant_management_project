from django.contrib import admin
from django.utils import timezone
from .models import Reservation

class ReservationStatusFilter(admin.SimpleListFilter):
    title = 'Reservation Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('upcoming', 'Upcoming'),
            ('past', 'Past'),
        ]

    def queryset(self, request, queryset):
        now = timezone.now()
        value = self.value()

        if value == 'upcoming':
            return queryset.filter(reservation_datetime__gte=now)
        elif value == 'past':
            return queryset.filter(reservation_datetime__lt=now)
        return queryset


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reservation_datetime', 'table', 'status')
    list_filter = (ReservationStatusFilter,)  # 👈 add custom filter here
