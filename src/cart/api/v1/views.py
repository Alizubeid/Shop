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


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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
