from django.db import models
from django.db.models import Q

class TableManager(models.Manager):
    def get_available_tables(self, date, time, capacity=None):
        from orders.models import Reservation  # to avoid circular import

        # Step 1: Find tables that are already reserved for given date & time
        reserved_tables = Reservation.objects.filter(
            Q(date=date) & Q(time=time)
        ).values_list('table_id', flat=True)

        # Step 2: Exclude reserved tables
        available_tables = self.exclude(id__in=reserved_tables)

        # Step 3: Optional filter for capacity
        if capacity:
            available_tables = available_tables.filter(capacity__gte=capacity)

        return available_tables

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    # Attach custom manager
    objects = TableManager()

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
