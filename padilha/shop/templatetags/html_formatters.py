from django import template

def currency_euro(value):
    return f"{value:.2f} €"

def productimage(value):
    return f"https://raw.githubusercontent.com/pythonforeveryonetraining/gennaroshop/main/products/{value}"

register = template.Library()

register.filter("currency_euro", currency_euro) # name the filter, function
register.simple_tag(productimage)    