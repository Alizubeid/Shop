from datetime import datetime
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
    def __str__(self):
        return f"{self.category}"
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(null=True, upload_to=f"products/%y/%m/%d/{name}")
    price = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="product_company")
    category = models.ManyToManyField(Category)


    def discount(self):
        if dis:=Discount.objects.filter(product=self):
            discount = dis.first()
            if dis:=discount.amount>0:
                return (self.price - dis)
            elif dis:=discount.percent>0:
                return (self.price * dis / 100)
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name



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
    amount = models.PositiveIntegerField(default=0,null=True)
    percent = models.PositiveIntegerField(default=0,null=True)
    
    def __str__(self):
        return f"{self.product.name or self.category.category} - {f'{self.amount}$' if self.amount else f'{self.percent}%' if {self.percent} else ''}"
    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیفات"    

class Cart(models.Model):
    Status=[
        ("1","in progress"),
        ("2","confirmed"),
        ("3","SEND")
    ]
        

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField(default=0,null=True)
    date = models.DateTimeField(default=timezone.now,null=True)
    status = models.CharField(max_length=64,choices=Status,default="1",null=True)


    def __str__(self):
        return f"{self.customer} - {self.total_amount}"


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="cart")
    item = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_item")
    quntity = models.PositiveIntegerField(default=0,null=True)
    total_amount = models.PositiveIntegerField(default=0,null=True)
    
    def save(self, *args, **kwargs):
        self.total_amount = (self.item.price * self.quntity)
        self.cart.total_amount += self.total_amount
        self.cart.save()
        return super(CartItems,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.cart} ~ {self.item} ~ {self.quntity} ~ {self.total_amount}"



