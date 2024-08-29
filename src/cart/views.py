from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from cart.models import Cart, CartItems, Product
from django.views.generic.base import View,TemplateView
from django.views.generic.list import ListView

from vendors.models import Company,Companies,Staff


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
