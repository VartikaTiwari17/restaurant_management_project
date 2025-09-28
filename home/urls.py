from django.urls import path
from .view import ContactFormSubmissionView


urlpatterns = [
    path('api/contact/', ContactFormSubmissionView.as_view() name='contact-form-submit'),
]