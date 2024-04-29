from django.urls import path
from shop.views.indexview import IndexView
from shop.views.productdetailsview import ProductDetailsView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/<int:id>", ProductDetailsView.as_view(), name="products")
]