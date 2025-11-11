from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackSubmissionAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
