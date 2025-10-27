from .views import HolidayHoursListView

urlpatterns = [
    # ... other paths
    path('api/holiday-hours/', HolidayHoursListView.as_view(), name='holiday-hours-list'),
]
