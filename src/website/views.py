from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from vendors.models import Company
from cart.models import Product
from vendors.models import Staff
from accounts.models import Address, Profile
from .utils import ProductFilter
from django_filters.views import FilterView
from accounts.models import User
from accounts.forms import AddressForm, ProfileForm

class NavbarUserTypeMixin(object):
    class UserType:
        def __init__(self, user: User):
            self.user = user
            self._company = None
            self.profile = None
            self._user_type = None
            self.is_satff = None

        def get_profile(self):
            if self.user_type != "goust":
                self.profile = Profile.objects.get(user=self.user)
                return self.profile

        def get_user_type_and_fix_staff(self):
            if self.user.is_authenticated:
                if self.user.is_staff:
                    if self.user.is_owner:
                        self._user_type = "owner"
                        self.is_satff = True
                        self._company = Company.objects.get(owner=self.user)
                    else:
                        staff = Staff.objects.get(user=self.user)
                        self.is_satff = True
                        self._company = staff.company
                        if staff.is_manager:
                            self._user_type = "manager"
                        elif staff.is_operator:
                            self._user_type = "operator"
                elif self.user.is_customer:
                    self._user_type = "customer"
            else:
                self._user_type = "goust"
            return self._user_type

        @property
        def image(self):
            if self._user_type != "goust":
                return self.profile.image.url

        @property
        def user_type(self):
            return self._user_type
        
        @property
        def company(self):
            return self._company
        
        @property
        def products(self):
            if self.company:
                return Product.objects.filter(company=self.company)
        
        def validate(self):
            self.get_user_type_and_fix_staff()
            self.get_profile()
            return self
    
    def get_user(self):
        return self.UserType(self.request.user).validate()
    
    def get_context_data(self, **kwargs):
        context = super(NavbarUserTypeMixin, self).get_context_data(**kwargs)
        user = self.get_user()
        context["user_nav"], context["user_image"] = user.user_type, user.image
        return context


class OwnerOrCustomerRegisterView(NavbarUserTypeMixin, TemplateView):
    template_name = "register/signup.html"


class UserLoginView(NavbarUserTypeMixin, LoginView):
    template_name = "login.html"
    redirect_authenticated_user = reverse_lazy("root")


class ProductListView(NavbarUserTypeMixin, FilterView):
    template_name = "base.html"
    model = Product
    context_object_name = "products"
    filterset_class = ProductFilter

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.get_user()
        if user.is_satff:
            return user.products
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


class ProfileUserView(NavbarUserTypeMixin, TemplateView):
    template_name = "profile/profile_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        address = Address.objects.filter(user=user).first()
        context["address"] = (
            f"{address.country.upper()}, {address.state.upper()}, {address.city}"
        )
        context["profile"] = profile
        return context
    

class ProfileUserUpdateView(NavbarUserTypeMixin, UpdateView):
    template_name = "profile/update_profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.get_user().profile
    
class AddressUserUpdateView(NavbarUserTypeMixin, UpdateView):
    template_name = "profile/address_update.html"
    form_class = AddressForm
    success_url = reverse_lazy("profile")

    def get_object(self):
        return Address.objects.get(user=self.request.user)