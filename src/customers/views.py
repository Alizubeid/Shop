from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from accounts.forms import AddressForm, ProfileForm
from accounts.models import Address, Profile
from customers.forms import RegisterForm
from website.views import NavbarUserTypeMixin


class CustomerRegisterView(NavbarUserTypeMixin, CreateView):
    template_name = "register/register_customer.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = ProfileForm
        context["address"] = AddressForm
        return context

    def form_valid(self, form):
        profile = ProfileForm(self.request.POST, self.request.FILES)
        address = AddressForm(self.request.POST)
        if profile.is_valid():
            print("true")
        if profile.is_valid() and address.is_valid():
            user = form.save()
            profile.instance.user = user
            profile = profile.save()
            address.instance.user = user
            address = address.save()
        return super().form_valid(form)
    