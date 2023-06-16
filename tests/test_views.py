from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token

from restaurant.models import Menu,Boking
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate
from restaurant.serializers import MenuSerializer
from rest_framework import status, request


# Create your tests here.

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testuser')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu1 = Menu.objects.create(title='Fish', price=80, inventory=10)
        self.menu1 = Menu.objects.create(title='Goat', price=80, inventory=10)

    def test_getall(self):
        url = reverse('menu-view')
        response = self.client.get(url)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        # request = self.client.get(reverse('menu-view'))
        # force_authenticate(request, user=None)
        # response = self.client.get(request)
        self.assertEqual(response.data, serializer.data)
        self.assert_(response.status_code, status.HTTP_200_OK)
