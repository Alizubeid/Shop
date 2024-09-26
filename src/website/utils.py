from cart.models import Product
from django_filters import FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ["name","company"]