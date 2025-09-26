from django.urls import path
from .view import MenuItemSearchSet

menu_item_search = MenuItemSearchViewSet.as_view({"get": "list"})


urlpatterns = [
   path("items/serach", menu_item_search, name="menu-item-search"),
]
