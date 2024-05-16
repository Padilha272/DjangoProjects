# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartDetail.as_view(), name='cart-detail'),
    path('cart/items/', views.CartItemListCreate.as_view(), name='cart-item-list-create'),
    path('orders/', views.OrderListCreate.as_view(), name='order-list-create'),
    path('checkout/', views.checkout, name='checkout'),
]
