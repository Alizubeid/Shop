from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.base import View
from accounts.forms import ProfileForm, AddressForm
from vendors.models import Manager, Operator, Companies
from vendors.forms import (
    OwnerCreationForm,
    ManagerCreationForm,
    OperatorCreationForm,
    CompanyCreationForm,
)
from shapeshifter.views import MultiFormView
from accounts.models import User
from website.views import NavbarUserTypeMixin


class OwnerCreateView(NavbarUserTypeMixin, FormView):
    template_name = "register/register_owner.html"
    form_class = OwnerCreationForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = ProfileForm
        context["address"] = AddressForm
        context["company"] = CompanyCreationForm
        return context

    def form_valid(self, form):

        profile = ProfileForm(self.request.POST, self.request.FILES)
        address = AddressForm(self.request.POST)
        company = CompanyCreationForm(self.request.POST)
        if profile.is_valid() and address.is_valid() and company.is_valid():
            user = form.save()
            profile.instance.user = user
            profile = profile.save()
            address.instance.user = user
            address = address.save()
            company.instance.owner = user
            company.instance.image = profile.image
            company = company.save()
            Companies.objects.create(
                company=company, address=address, is_main=True
            ).save()

        return super().form_valid(form)


class ManagerCreateView(FormView):
    template_name = "signup_staff.html"
    model = Manager
    form_class = ManagerCreationForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form):
        cd = form.cleaned_data
        user = User.objects.create(email=cd.get("email"), password=cd.get("password"))
        staff = Manager.objects.create(user=user)
        user.save()
        staff.save()
        return super().form_valid(form)


class OperatorCreateView(FormView):
    template_name = "signup_staff.html"
    form_class = OperatorCreationForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form):
        cd = form.cleaned_data
        user = User.objects.create(email=cd.get("email"), password=cd.get("password"))
        staff = Operator.objects.create(user=user)
        user.save()
        staff.save()
        return super().form_valid(form)
