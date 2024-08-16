from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from customers.models import Customer
from customers.forms import RegisterForm

class CustomerRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "signup.html"
    success_url = "/"
