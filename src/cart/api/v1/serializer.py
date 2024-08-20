from rest_framework import serializers
from cart.models import Product, Category


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.CharField()
    add_cart = serializers.URLField()

    class Meta:
        model = Product
        fields = ["name","price","add_cart","discount"]
