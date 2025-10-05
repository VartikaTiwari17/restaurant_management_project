from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import UserReview
from .serializers import UserReviewSerializer


class UserReviewCreateAPIView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permissions_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
     

     class MenuItemReviewAPIView(generics.ListAPIView):
        serializer_class = UserReviewSerializer


        def get_queryset(self):
            menu_item = self.kwargs.get('menu_item_id')
            return UserReview.objects.filter(menu_item__id=menu_item_id)
