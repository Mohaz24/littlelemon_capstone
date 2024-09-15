from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Menu, Booking
from .serialize import MenuSerializer, BookingSerializer

# Create your views here.
class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serialize_items = MenuSerializer(items, many=True)
        return Response(serialize_items.data, status.HTTP_200_OK)
 
    def post(self, request):
        serialize_items = MenuSerializer(data=request.data)
        if serialize_items.is_valid(raise_exception=True):
            serialize_items.save()
        return Response(serialize_items.data, status.HTTP_201_CREATED)
    
class SingleMenuView(APIView):
    def get(self, request, pk):
        items = get_object_or_404(Menu, pk=pk)
        serialize_items = MenuView(items)
        return Response(serialize_items.data, status.HTTP_200_OK)
    
class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serialize_items = BookingSerializer(items, many=True)
        return Response(serialize_items.data, status.HTTP_200_OK)
   
    def post(self, request):
         serialize_items = BookingSerializer(data=request.data)
         if serialize_items.is_valid(raise_exception=True):
             serialize_items.save()
         return Response(serialize_items.data, status.HTTP_201_CREATED)