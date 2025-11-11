from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackStatusSerializer

class FeedbackStatusUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to update the status of a feedback entry (admin only).
    Example: PATCH /api/feedback/1/status/ { "status": "approved" }
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        feedback = self.get_object()
        serializer = self.get_serializer(feedback, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Feedback status updated successfully.",
            "feedback": serializer.data
        }, status=status.HTTP_200_OK)
