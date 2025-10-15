from .django.db import ModelSerializer
from .models import UserReview




class UserReviewSerializer(serializer.ModelSerializer):
    user_name = serializer.CharField(source='user.username', read_only=True)


    class Meta:
        model = MenuItem
        fields = ['id', name','description','price', 'image' 'is_available']   # Only essential details
         