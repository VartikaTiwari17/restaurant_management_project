from rest_framework import generics
from home.models import Allergen
from home.serializers import AllergenSerializer

class AllergenListView(generics.ListAPIView):
    """
    API endpoint that returns a list of all available allergens.
    """
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
