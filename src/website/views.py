from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from vendors.models import Company
from cart.models import Product
from vendors.models import Staff
from accounts.models import Address, Profile


class NavbarUserTypeMixin(object):
    def user_type(self):
        user = self.request.user
        image = None
        if user.is_authenticated:
            profile = Profile.objects.filter(user=user).first()
            if profile:
                get_image = profile.image.url
                image = get_image
            if user.is_staff:
                if user.is_owner:
                    return "owner", image
                else:
                    staff = Staff.objects.filter(user=user).first()
                    if staff:
                        if staff.is_manager:
                            return "manager", image
                        elif staff.is_operator:
                            return "operator", image
                    else:
                        return "goust", image
            elif user.is_customer:
                return "customer", image
        else:
            return "goust", image

    def get_context_data(self, **kwargs):
        context = super(NavbarUserTypeMixin, self).get_context_data(**kwargs)
        context["user_nav"], context["user_image"] = self.user_type()
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

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            if user.is_owner:
                return qs.filter(company=Company.objects.get(owner=user))
        else:
            return qs
        
    
    


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

class ProfileUserView(NavbarUserTypeMixin,TemplateView):
    template_name = "profile/profile_view.html"



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        address = Address.objects.filter(user=user).first()
        context["address"] = f"{address.country.upper()}, {address.state.upper()}, {address.city}"
        context["profile"] = profile
        return context
    