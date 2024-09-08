from django import forms
from customers.models import Customer
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["email"]
    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

