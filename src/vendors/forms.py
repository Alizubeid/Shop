from django import forms
from vendors.models import Owner, Manager, Operator
from django.contrib.auth.forms import UserCreationForm


class OwnerCreationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = ["email"]

class ManagerCreationForm(forms.Form):
    email = forms.EmailField(max_length=64,widget=forms.EmailInput)
    password = forms.CharField(max_length=64,widget=forms.PasswordInput)


class OperatorCreationForm(forms.Form):
    email = forms.EmailField(max_length=64,widget=forms.EmailInput)
    password = forms.CharField(max_length=64,widget=forms.PasswordInput)