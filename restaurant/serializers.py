from django.contrib.auth.models import User

from .models import Menu, Boking
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['username','email','password']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boking
        fields = '__all__'