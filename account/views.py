from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserLoyaltyPointsSerializer
from .utils import get_user_total_loyalty_points

class UserLoyaltyPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        total_points = get_user_total_loyalty_points(user)
        serializer = UserLoyaltyPointsSerializer({'total_points': total_points})
        return Response(serializer.data)
