from django.db import models
from vendors.models import Company
from accounts.models import User
from django.utils import timezone


def today():
    return timezone.now().date


class Category(models.Model):
    category = models.CharField(max_length=64)
    sub_category = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="category_sub_category",
    )
    def __str__(self):
        return f"{self.category}"
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(null=True, upload_to=f"products/%y/%m/%d/{name}")
    price = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def add_cart(self):
        return f"http://127.0.0.1:8000/cart/add_cart/{self.pk}/"

    def discount(self):
        obj = Discount.objects.filter(product=self).first()
        if obj:
            if obj.amount > 0:
                return f"{obj.amount}$"
            elif obj.percent > 0:
                return f"{obj.percent}%"
        else:
            return 0
    def __str__(self):
        return f"{self.name} - {self.price} - {self.company} "
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product/%y/%m/%d/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Property(models.Model):
    property_field = models.CharField(max_length=64)

    def __str__(self):
        return self.property_field


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    property_field = models.ForeignKey(Property, on_delete=models.CASCADE)
    value = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.product} - {self.property_field}"


class Discount(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name or self.category.category} - {f'{self.amount}$' if self.amount else f'{self.percent}%' if {self.percent} else ''}"
    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیفات"    

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField(default=0)
    # total_amount_with_discount = models.PositiveIntegerField(default=0)
    date = models.DateField(null=True, default=today)
    is_paid = models.BooleanField(default=False)

    def paid(self):
        self.is_paid = True
    
    def __str__(self):
        return f"{self.customer} - {self.total_amount}"


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField(default=0)
    quntity = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)
    total_amount_with_discount = models.PositiveIntegerField(default=0)

    def add_quntity(self):
        self.quntity += 1
        self.save()

    def odd_quntity(self):
        self.quntity -= 1
        self.save()

