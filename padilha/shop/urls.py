from django.urls import path
from shop.views.indexview import IndexView
from shop.views.productdetailsview import ProductDetailsView
from shop.views.registrationview import register
from django.contrib.auth.views import LogoutView
from shop.views.loginview import user_login,user_logout


urlpatterns = [
    path("categories/<int:id>", IndexView.as_view(), name="categories"),
    path("products/<int:id>", ProductDetailsView.as_view(), name="products"),
    path("", IndexView.as_view(), name="index"),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('logout/', user_logout, name='logout')
    
    
]