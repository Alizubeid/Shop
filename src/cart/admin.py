from django.contrib import admin
from cart.models import Cart, CartItems, Discount, Product, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Cart)
admin.site.register(CartItems)
