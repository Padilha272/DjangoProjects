from django.urls import path
from variety.views.view import VarietyHtml
from django.views.generic import TemplateView

urlpatterns=[
    path("", VarietyHtml.as_view(), name="view"),
    path("title/", TemplateView.as_view(
        template_name="variety/title.html"
    ), name="title"),   
]

