# home/urls.py
from .views import MenuCategoryWithCountView

urlpatterns = [
    # ... existing endpoints
    path('api/menu/categories-with-count/', MenuCategoryWithCountView.as_view(), name='menu-categories-with-count'),
]
