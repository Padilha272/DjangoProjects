# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),  # Corrigido aqui
    path('cart/items/', views.CartItemListCreate.as_view(), name='cart-item-list-create'),
    path('orders/', views.OrderListCreate.as_view(), name='order-list-create'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
]
