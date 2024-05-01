from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Category

#A class based view wil have a get method, which will return a
#modified get method
class IndexView(TemplateView):
    template_name="shop/index.html"
    
    def get(self, request, id=None):
        categories = Category.objects.order_by("name")
        if id is None: 
            title = "All products"          
            products = Product.objects.order_by("name")
        else:
            title = next(c.name for c in categories if c.id ==id)
            products = Product.objects.filter(category_id=id).order_by("name")
        context = {
            "categories": [{"id":c.id,"name":c.name} for c in categories],
            "title": title,
            "products":[{"id" : p.id,"name":p.name, "price":p.price ,"image": p.image} for p in products]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context,request))
    
