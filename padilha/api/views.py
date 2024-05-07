from django.shortcuts import render

# api/views.py
from rest_framework import generics
from shop.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

