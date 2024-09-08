from django import template
from cart.models import ProductImage

register = template.Library()

@register.filter
def product_image(obj):
    return ProductImage.objects.filter(product=obj)

@register.filter
def navbar(obj):
    return f"nav/{obj}.html"


