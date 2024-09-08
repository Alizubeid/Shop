from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from vendors.models import Company
from cart.models import Product
from vendors.models import Staff
from accounts.models import Profile


class NavbarUserTypeMixin(object):
    def user_type(self):
        user = self.request.user
        if user.is_authenticated:
            if profile := Profile.objects.filter(user=user).first():
                if image := profile.image:
                    image = image.url
            if user.is_staff:
                if user.is_superuser:
                    return "goust", image
                if user.is_owner:
                    return "owner", image
                else:
                    user = Staff.objects.filter(user=user).first()
                    if user.is_manager:
                        return "manager", image
                    elif user.is_operator:
                        return "operator", image
                    else:
                        return "goust", False
            else:
                return "customer", image
        else:
            return "goust", False

    def get_context_data(self, **kwargs):
        context = super(NavbarUserTypeMixin, self).get_context_data(**kwargs)
        context["user_nav"], context["user_image"] = self.user_type()
        print(self.user_type())
        return context


class OwnerOrCustomerRegisterView(NavbarUserTypeMixin, TemplateView):
    template_name = "register/signup.html"


class UserLoginView(NavbarUserTypeMixin, LoginView):
    template_name = "login.html"
    redirect_authenticated_user = reverse_lazy("root")


class ProductListView(NavbarUserTypeMixin, ListView):
    template_name = "base.html"
    model = Product
    context_object_name = "products"


class ProductCompanyListView(NavbarUserTypeMixin, ListView):
    template_name = "base.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        name_company = self.kwargs.get("name")
        return qs.filter(company__company_name=name_company)


class CompanyListView(NavbarUserTypeMixin, ListView):
    template_name = "shops.html"
    queryset = Company.objects.all()
    context_object_name = "shops"
