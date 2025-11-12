from rest_framework import serializers

class UserLoyaltyPointsSerializer(serializers.Serializer):
    total_points = serializers.IntegerField(read_only=True)
