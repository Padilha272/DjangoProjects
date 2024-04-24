from django.views.generic import TemplateView
from django.http import HttpResponse

class IndexView(TemplateView):
    def get(self, request):
        return HttpResponse("Padilha webshop")