from django.urls import path
from .views import ContactMessageListAPIView

urlpatterns = [
    path('api/contact-messages/', ContactMessageListAPIView.as_view(), name='contact_messages_list'),
]
