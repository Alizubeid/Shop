from django.contrib import admin
from cart.models import Discount, Product, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
