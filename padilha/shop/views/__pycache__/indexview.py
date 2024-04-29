from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

#A class based view wil have a get method, which will return a
#modified get method
class IndexView(TemplateView):
    template_name="shop/index.html"
    
    def get(self, request):
        products = Product.objects.order_by("name")
        context = {"products":[{"name":p.name, "price":p.price} for p in products]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context,request))
    
