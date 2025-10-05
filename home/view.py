from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import DailySpecialSerializer


@api_view(['GET'])
def daily_specials(request):
    specials = MenuItem.objects.filter(is_daily_special=True)
    serializer = DailySpecialSerializer(specials, many=True)
    return Response(serializer.data)
