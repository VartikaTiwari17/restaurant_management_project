from django.urls import path
from .views import AddFavoriteMenuItemAPIView

urlpatterns = [
    path('favorites/add/', AddFavoriteMenuItemAPIView.as_view(), name='add_favorite'),
]
