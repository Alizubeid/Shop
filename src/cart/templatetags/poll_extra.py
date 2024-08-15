from django import template
from cart.models import ProductImage

register = template.Library()

def product_image(obj):
    return ProductImage.objects.filter(product=obj)