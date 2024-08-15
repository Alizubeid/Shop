from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from cart.models import Product,ProductImage

class ProductsListView(ListView):
    model = Product

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["images"] = ProductImage.objects.all()
ProductImage