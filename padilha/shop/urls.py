from django.urls import path
from shop.views.indexview import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]