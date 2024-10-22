import json
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from cart.models import Product, Cart, CartItems
from website.views import NavbarUserTypeMixin
from django.views.generic.base import TemplateView
from website.views import NavbarUserTypeMixin


class ProductAPIView(NavbarUserTypeMixin,generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        user = self.get_user()
        if user.is_satff:
            return qs.filter(company=user.company)
        return qs

class CartItemsView(NavbarUserTypeMixin,generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        cookie = self.request.COOKIES
        try:
            data = cookie.pop("cart")
            if data:
                data_parse = dict(json.loads(data))
                items = [int(product_id) for product_id,product_quntity in data_parse.items()]
                return qs.filter(pk__in=items)
        except KeyError:
            pass




class CheckOutCart(NavbarUserTypeMixin, TemplateView):
    def get_template_names(self):
        cookie = self.request.COOKIES
        try:
            data = cookie.pop("cart")
            if data:
                data_parse = dict(json.loads(data))
                cart = Cart.objects.create(customer=self.request.user)
                for product, quntity in data_parse.items():
                    product_obj = Product.objects.get(pk=int(product))
                    item = CartItems.objects.create(
                        cart=cart,
                        item=product_obj, 
                        quntity=quntity
                    )
                self.request.COOKIES = cookie
                return ["thankyou.html"]
            else:
                return ["base.html"]
        except KeyError:
            return ["base.html"]

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)    
        response.delete_cookie("cart")
        return response
