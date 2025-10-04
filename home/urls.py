from django.urls import path
from .view import AvailableTablesAPIView


urlpatterns = [
    path('api/tables/available/', AvailablesTablesAPIView.as_view() name='available_tables_api'),
]