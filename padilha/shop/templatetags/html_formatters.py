from django import template

register = template.Library()

@register.filter
def currency_euro(value):
    return f"{value:.2f} €"

@register.simple_tag
def productimage(value):
    return f"https://raw.githubusercontent.com/pythonforeveryonetraining/gennaroshop/main/products/{value}"



register.filter("currency_euro", currency_euro)
register.simple_tag(productimage)
