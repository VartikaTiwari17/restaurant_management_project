from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListView(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all().order_by('-id')
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
