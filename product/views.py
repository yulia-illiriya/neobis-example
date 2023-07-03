from django.shortcuts import render

from rest_framework import generics
from .models import Price, Photo, Product
from .serializers import PhotoSerializer, ProductSerializer, PriceSerializer
 

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
