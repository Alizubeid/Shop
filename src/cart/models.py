from django.db import models
from vendors.models import Company
from accounts.models import User


class Category(models.Model):
    category = models.CharField(max_length=64)
    sub_category = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.CASCADE,
        related_name="category_sub_category",
    )


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    date_pd = models.DateField()
    date_ex = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)


class Property(models.Model):
    property_field = models.CharField(max_length=64)


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    property_field = models.ForeignKey(Property, on_delete=models.CASCADE)
    value = models.CharField(max_length=64)


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(null=True)
    percent = models.PositiveIntegerField(null=True)


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField(default=0)
    date = models.DateField()
    is_paid = models.BooleanField(default=False)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
