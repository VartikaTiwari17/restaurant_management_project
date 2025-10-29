from django.urls import path
from .views import UserLoyaltyPointsView

urlpatterns = [
    path('api/my-loyalty-points/', UserLoyaltyPointsView.as_view(), name='user-loyalty-points'),
]
