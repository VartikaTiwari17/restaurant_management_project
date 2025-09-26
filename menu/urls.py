from django.urls import path
from .view import MenuItemByCategoryView


urlpatterns = [
   path("items/", MenuItemByCategoryView.as_View(), name="menu-item-by-category"),
]
