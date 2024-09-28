from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from cart.models import Product

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CheckOutCart(APIView):
    def get(self, request, pk, format=None):
        pass