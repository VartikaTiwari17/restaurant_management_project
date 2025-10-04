from django.urls import path
from .view import AvailableTablesAPIView,  TableDetailAPIView


urlpatterns = [
    path('api/tables/available/', AvailablesTablesAPIView.as_view() name='available_tables_api'),
    path('api/tables/<int:pk>/',  TabledetailAPIView.as_view(),  name='table_detail_api')
]