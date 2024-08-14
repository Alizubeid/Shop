from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Profile


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "is_owner", "is_customer"]


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = visible.field.label

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone_number", "birth", "gender"]
