from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import SignupForm

class SignUpView(FormView):
    form_class = SignupForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
