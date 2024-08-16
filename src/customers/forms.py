from django import forms
from customers.models import Customer
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["email"]
