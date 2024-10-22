from rest_framework import serializers
from cart.models import Product, Category


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
