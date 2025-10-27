from django.urls import path
from .views import StaffShiftListView

urlpatterns = [
    path('api/shifts/', StaffShiftListView.as_view(), name='staff-shift-list'),
]
