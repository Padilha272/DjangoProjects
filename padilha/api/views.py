# api/views.py
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer, CategorySerializer,ProductSerializer
from shop.models import Product, Category

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart

class CartItemListCreate(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart.items.all()

    def perform_create(self, serializer):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        product_id = self.request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            serializer.save(cart=cart, product=product)

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
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        cart_items = cart.items.all()
        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        order = serializer.save(user=user, total_amount=total_amount)
        for item in cart_items:
            order.items.add(item)
        cart.items.all().delete()
        cart.delete()

@api_view(['POST'])
def add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def remove_from_cart(request, product_id):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    product = get_object_or_404(Product, pk=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def checkout(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    cart_items = cart.items.all()
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=user, total_amount=total_amount)
    for cart_item in cart_items:
        order.items.add(cart_item)
        cart_item.delete()
    cart.delete()
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})

@login_required
def order_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order.html', {'orders': orders})

@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'checkout.html', {'cart': cart})

@login_required
def order_confirmation_view(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        total_amount = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(user=request.user, total_amount=total_amount)

        for cart_item in cart_items:
            order.items.add(cart_item)
            cart_item.delete()

        order.save()

        return render(request, 'order_confirmation.html', {'order': order})
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)