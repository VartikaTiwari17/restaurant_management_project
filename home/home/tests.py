form rest_framework .test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Restaurant




class RestaurantInfoTest(APITestCase):


    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name ='Test Restaurant',
            address= '123 Test St',
            phone_number ='1234567890',
            email='test@example.com'
        )


        self.url = reverse('restaurant-info')