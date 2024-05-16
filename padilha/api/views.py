from django.shortcuts import render

# api/views.py
from rest_framework import generics
from shop.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart,CartItem, Order
from .serializers import CartSerializer,CartItemSerializer, OrderSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart
    
class CartItemListCreate(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart.items.all()

    def perform_create(self, serializer):
        user = self.request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        serializer.save(cart=cart)

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
def add_to_cart(request, product_id):
    user = request.user
    try:
         cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)

    product = Product.objects.get(pk=product_id)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def remove_from_cart(request, product_id):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response({"error": "Cart does not exist."}, status=status.HTTP_404_NOT_FOUND)
    except Product.DoesNotExist:
        return Response({"error": "Product not found in cart."}, status=status.HTTP_404_NOT_FOUND)
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def checkout(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = cart.items.all()
    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(user=user, total_amount=total_amount)

    for cart_item in cart_items:
        order.items.add(cart_item)
        cart_item.delete()

    serializer = OrderSerializer(order)
    return Response(serializer.data)

class CartDetailAPIView(APIView):
    def get(self, request, format=None):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user = request.user
        cart = Cart.objects.get(user=user)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartItemListAPIView(APIView):
    def get(self, request, format=None):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        items = cart.items.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)