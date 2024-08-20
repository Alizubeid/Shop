from django.db import models
from vendors.models import Company
from accounts.models import User
from django.utils import timezone



class Category(models.Model):
    category = models.CharField(max_length=64)
    sub_category = models.ForeignKey(
        "self",
        null=True,
        blank=True,
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

    def add_cart(self):
        return f"http://127.0.0.1:8000/api/add_cart/{self.pk}/"
    
    def discount(self):
        obj = Discount.objects.filter(product=self).first()
        if obj:
            if obj.amount>0:
                return f"{obj.amount}$"
            elif obj.percent>0:
                return f"{obj.percent}%"
        else:
                return 0



class ProductImage(models.Model):
    image = models.ImageField(upload_to="product/%y/%m/%d/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Property(models.Model):
    property_field = models.CharField(max_length=64)


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    property_field = models.ForeignKey(Property, on_delete=models.CASCADE)
    value = models.CharField(max_length=64)


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=0)
    percent = models.PositiveIntegerField(default=0)


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField(default=0)
    total_amount_with_discount = models.PositiveIntegerField(default=0)
    date = models.DateField(null=True)
    is_paid = models.BooleanField(default=False)

    def paid(self):
        self.date = timezone.now().date
        self.is_paid = True


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField()
    quntity = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    total_amount_with_discount = models.PositiveIntegerField()
