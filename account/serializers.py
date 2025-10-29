from rest_framework import serializers
from django.contrib.auth.models import User  # or your custom user model

class UserLoyaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['loyalty_points']
