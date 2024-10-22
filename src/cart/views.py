from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from cart.models import Cart, CartItems, Discount, Product
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import RedirectView
from vendors.models import Company, Companies, Staff
from website.views import NavbarUserTypeMixin
from .forms import AddProductForm, DiscountCategoryForm, DiscountProductForm,StatusProductView
from django.views.generic.edit import FormView
import json


class AddCartView(View):

    def get(self, *args, **kwargs):
        cart = Cart.objects
        user_login = self.request.user
        user_cart = cart.filter(customer=user_login, is_paid=False)
        product = Product.objects.get(pk=self.kwargs.get("pk"))
        if user_cart:
            print("cart is valid")
            user_cart = user_cart.first()
            if order_item := CartItems.objects.filter(cart=user_cart, item=product):
                print("add product again")
                order_item.first().add_quntity()
                order_item.update()
            else:
                print("add product")
                order_item = CartItems.objects.create(cart=user_cart, item=product)
                order_item.add_quntity()
                order_item.save()

        else:
            print("new cart")
            user_cart = cart.create(customer=user_login)
            order_item = CartItems.objects.create(
                cart=user_cart, item=product, quntity=1
            )
            user_cart.save()
            order_item.save()
        return redirect("product-list-view-API")


class CustomerCartHistory(ListView):
    model = Cart

    def get_queryset(self):
        qs = super().get_queryset()
        cart = qs.filter(customer=self.request.user, is_paid=True)


class CompanyCartHistory(TemplateView):
    template_name = "comapny.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            print(user.is_owner)
            if user.is_owner:
                company = Company.objects.filter(owner=user)
            else:
                company = (
                    Staff.objects.filter(user=user)
                    .select_related("company")
                    .select_related("company")
                    .first()
                    .company.company
                )
            return company

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["company"] = self.get_queryset()
        return context


class AddProductView(NavbarUserTypeMixin, CreateView):
    template_name = "products/add_product.html"
    form_class = AddProductForm
    success_url = reverse_lazy("root")

    def form_valid(self, form):
        user = self.request.user
        form.instance.company = Company.objects.get(owner=user)
        return super().form_valid(form)


class UpdateProductView(NavbarUserTypeMixin, UpdateView):
    template_name = "products/add_product.html"
    form_class = AddProductForm
    model = Product
    success_url = reverse_lazy("root")


class DiscountChoise(NavbarUserTypeMixin, TemplateView):
    template_name = "discount/choice.html"


class AddProductDiscount(NavbarUserTypeMixin, CreateView):
    template_name = "discount/set_product.html"
    form_class = DiscountProductForm
    success_url = reverse_lazy("root")

    def form_valid(self, form):
        type_discount = int(form.cleaned_data.get("type_discount"))
        amount = int(form.cleaned_data.get("number"))
        form.instance.company = self.get_user().company

        if int(type_discount) == 1:
            form.instance.amount = amount
            return form
        elif int(type_discount) == 2:
            form.instance.percent = amount
            return form



class AddCategoryDiscount(NavbarUserTypeMixin, CreateView):
    template_name = "discount/set_category.html"
    form_class = DiscountCategoryForm
    success_url = reverse_lazy("root")

    def form_valid(self, form):
        type_discount = form.cleaned_data.get("type_discount")
        amount = form.cleaned_data.get("number")
        form.instance.company = self.get_user().company

        if int(type_discount) == 1:
            form.instance.amount = amount
            return form
        elif int(type_discount) == 2:
            form.instance.percent = amount
            return form
        

class ProductItemView(NavbarUserTypeMixin,ListView):
    template_name = "cart.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        cart = self.request.COOKIES.get("cart")
        if cart:
            return qs.filter(pk__in=[int(pk) for pk in json.loads(cart)])

class ThankYouView(NavbarUserTypeMixin,TemplateView):
    template_name = "thankyou.html"


class CartHistoryView(NavbarUserTypeMixin,ListView):
    model = Cart
    template_name = "cart_history.html"
    context_object_name = "carts"

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        user = self.get_user()
        if user.user:
            if user.is_satff:
                carts=[]
                for cart_item in CartItems.objects.filter(item__company=user.company):
                    cart = cart_item.cart
                    if cart not in carts:
                        carts.append(cart)
                return carts
            else:
                return qs.filter(customer=user.user)

class CartItemsView(NavbarUserTypeMixin,ListView):
    model = CartItems
    template_name = "cart_item.html"
    context_object_name = "items"

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.get_user()
        if user.user:
            if user.is_satff:
                return qs.select_related("item","cart").filter(cart__pk=self.kwargs.get("pk"),item__company=user.company)
            return qs.select_related("item").filter(cart__pk=self.kwargs.get("pk"))
        
class UpdateStatusCartItem(NavbarUserTypeMixin,UpdateView):
    template_name = "products/change_status.html"
    form_class = StatusProductView
    model = CartItems
    success_url = reverse_lazy("root")