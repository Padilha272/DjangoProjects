from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

#A class based view wil have a get method, which will return a
#modified get method
class ProductDetailsView(TemplateView):
    template_name="shop/productdetails.html"
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {
            "title": product.name,
            "description": product.description,
            "price": product.price,
            "volume:": product.volume,
            "image": product.image
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context,request))
    
