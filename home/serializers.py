from rest_framework import serializers
from .models import Feedback

class FeedbackStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'status']
