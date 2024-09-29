import json
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from cart.models import Product, Cart, CartItems
from website.views import NavbarUserTypeMixin


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CheckOutCart(NavbarUserTypeMixin, APIView):
    def get(self, request, format=None):
        cookie = self.request.COOKIES
        try:
            data = cookie.pop("cart")
            if data:
                data_parse = dict(json.loads(data))
                cart = Cart.objects.create(customer=self.request.user)
                cart.save()
                print(cart)
                for product, quntity in data_parse.items():
                    product_obj = Product.objects.get(pk=int(product))
                    print(product_obj)
                    item = CartItems.objects.create(
                        cart=cart,
                        item=product_obj, 
                        quntity=quntity
                    )
                    item.save()
                    print(item)

                response = Response({"status": "seccussfully"})
                for key, value in cookie.items():
                    response.set_cookie(key, value)

                return response
        except KeyError:
            return Response({"status": "faild"})
        return Response({"status": "faild"})
