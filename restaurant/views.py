from django.shortcuts import render

# Create your views here.
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Menu, Boking
from restaurant.serializers import MenuSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Boking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]

