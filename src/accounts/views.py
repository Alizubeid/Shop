from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from accounts.forms import SignupForm
from accounts.models import Profile, User, Address


class SignUpView(CreateView):
    model = User
    template_name = "base.html"
    form_class = SignupForm

class ProfileCreateView(CreateView):
    model = Profile
    fields = ["first_name", "last_name", "phone_number", "birth", "gender"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        # form.save()
        return super(ProfileCreateView,self).form_valid(form)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "index.html"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        qs = super().get_object(queryset)
        return qs.objects.get(user=self.request.user)


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "index.html"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        qs = super().get_object(queryset)
        return qs.objects.get(user=self.request.user)


class AddressCreateView(CreateView):
    model = Address
    fields = ["country", "state", "city", "street", "zip_code"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        # form.save()
        return super(AddressCreateView, self).form_valid(form)


class AddressListView(ListView):
    model = Address

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class AddressUpdateView(UpdateView):
    model = Address
    fields = ["country", "state", "city", "street", "zip_code"]
