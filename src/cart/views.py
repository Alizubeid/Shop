from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from cart.models import Cart, CartItems, Product
from django.views.generic.base import View,TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from vendors.models import Company,Companies,Staff
from website.views import NavbarUserTypeMixin
from .forms import AddProductForm

class AddCartView(View):

    def get(self,*args,**kwargs):
        cart = Cart.objects
        user_login = self.request.user
        user_cart = cart.filter(customer=user_login, is_paid=False)
        product = Product.objects.get(pk=self.kwargs.get("pk"))
        if user_cart:
            print("cart is valid")
            user_cart = user_cart.first()
            if order_item := CartItems.objects.filter(cart=user_cart, item=product):
                print("add product again")
                order_item.first().add_quntity()
                order_item.update()
            else:
                print("add product")
                order_item = CartItems.objects.create(cart=user_cart, item=product)
                order_item.add_quntity()
                order_item.save()

        else:
            print("new cart")
            user_cart = cart.create(customer=user_login)
            order_item = CartItems.objects.create(
                cart=user_cart, item=product, quntity=1
            )
            user_cart.save()
            order_item.save()
        return redirect("product-list-view-API")


class CustomerCartHistory(ListView):
    model = Cart
    def get_queryset(self):
        qs = super().get_queryset()
        cart = qs.filter(customer=self.request.user,is_paid=True)
    

class CompanyCartHistory(TemplateView):
    template_name = "comapny.html"
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            print(user.is_owner)
            if user.is_owner:
                company = Company.objects.filter(owner=user)
            else:
                company = Staff.objects.filter(user=user).select_related("company").select_related("company").first().company.company
            return company
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["company"] = self.get_queryset()
        return context

class AddProductView(NavbarUserTypeMixin,CreateView):
    template_name = "products/add_product.html"
    form_class = AddProductForm
    success_url = reverse_lazy("root")

    def form_valid(self, form):
        user = self.request.user
        form.instance.company = Company.objects.get(owner=user)
        return super().form_valid(form)

class UpdateProductView(NavbarUserTypeMixin,UpdateView):
    template_name = "products/add_product.html"
    form_class = AddProductForm
    model = Product
    success_url = reverse_lazy("root")