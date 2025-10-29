from django.urls import path
from home.views import AllergenListView

urlpatterns = [
    path('api/allergens/', AllergenListView.as_view(), name='allergen-list'),
]
