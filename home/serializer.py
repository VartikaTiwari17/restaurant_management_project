from rest_framework import serializers
from .models import UserReview


class UserReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
      class Meta:
         model = UserReview
         fields = ['id', 'name', 'menu_item', 'rating', 'comment', 'review_date']
         read_only_fields = ['id', 'review_date', 'user_name']



         def validate_rating(self,value):
            if value <1 or value>5:
                raise serializers.ValidationError("rating must be between 1 and 5.")
            return value
         