from django.shortcuts import render
from django.views.generic.list import ListView
from vendors.models import Company
from cart.models import Product

class ProductListView(ListView):
    template_name = "base.html"
    model=Product
    context_object_name="products"

    def get_queryset(self):
        qs = super().get_queryset()
        if name_company:=self.kwargs.get("name"):
            return qs.filter(company__company_name=name_company)
        return qs.all()
    


class CompanyListView(ListView):
    template_name = "shops.html"
    queryset = Company.objects.all()
    context_object_name = "shops"

