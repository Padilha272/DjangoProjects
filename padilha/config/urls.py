# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Certifique-se de que esta linha esteja presente
    path('', include('shop.urls')),
    path('variety/', include('variety.urls')),
    path('api/', include('api.urls')),
]
