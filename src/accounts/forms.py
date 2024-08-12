from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email","is_owner","is_customer","password"]
