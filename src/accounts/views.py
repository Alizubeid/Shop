from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from accounts.forms import SignupForm
from accounts.models import Profile, User


class SignUpView(CreateView):
    model = User
    template_name = "accounts/signup.html"
    form_class = SignupForm


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

