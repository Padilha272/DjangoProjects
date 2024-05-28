# config/urls.py
from django.contrib import admin
from django.urls import path, include
from shop.views.testview import test_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Certifique-se de que esta linha esteja presente
    path('', include('shop.urls')),
    path('variety/', include('variety.urls')),
    path('api/', include('api.urls')),
    path('test/',test_view,name="test_view")
]
