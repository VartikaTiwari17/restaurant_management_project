from rest_framework import generics
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer

class ActivePaymentMethodsListView(generics.ListAPIView):
    queryset = PaymentMethod.objects.filter(is_active=True)
    serializer_class = PaymentMethodSerializer
