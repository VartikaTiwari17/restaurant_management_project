from rest_framework import generics 
from .models import ContactFormSubumission
from .serializer import ContactFormSubumissionSerializer


class ContactFormSubmission(generics.CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer