# config/urls.py
from django.contrib import admin
from django.urls import path, include



#This is a place where we can add the routes to the applications
urlpatterns = [
    path('', include('shop.urls')),
    path('variety/',include('variety.urls')),
    path('admin/', admin.site.urls),
   
]
