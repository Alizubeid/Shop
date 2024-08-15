from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from cart.models import Product

class ProductsListView(ListView):
    model = Product
