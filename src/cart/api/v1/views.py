from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from cart.models import Product

class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = Product.objects.all().first()
        serialaizer = ProductSerializer(obj)
        # serialaizer.is_valid(raise_exception=True)
        return Response(serialaizer.data)
