from django.urls import path
from .views import add_to_cart, remove_from_cart, checkout, CartDetail, CartItemList

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', CartDetail.as_view(), name='cart_detail'),
    path('cart_items/', CartItemList.as_view(), name='cart_item_list'),
]
