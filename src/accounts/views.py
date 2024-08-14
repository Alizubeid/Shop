from typing import Any
from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import SignupForm, ProfileForm
from accounts.models import Profile


class SignUpView(FormView):
    template_name = "accounts/signup.html"
    form_class = SignupForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = "index.html"
    success_url = "/"

    def get_initial(self) -> dict[str, Any]:
        obj = Profile.objects.get(user=self.request.user)
