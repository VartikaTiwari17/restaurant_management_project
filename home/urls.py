from django.urls import path
from .view import MenuCategoryListAPIView


urlpatterns = [
    path('api/menu-categories/', MenuCategoryListAPIView.as_view() name='menu-categories-list'),
]