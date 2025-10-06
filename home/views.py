from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import UserReview
from .serializers import UserReviewSerializer


class MenuCategoryViewSet(viewset.ModelViewSet):
    queryset = MenuCategory.objects.all().order_vy('name')
    serializer_class = MenuCategorySerializer

