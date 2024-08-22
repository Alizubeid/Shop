from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from cart.models import Cart, CartItems, Product
from django.views.generic.base import RedirectView,View


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
