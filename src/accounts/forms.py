from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Profile,Address


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone_number", "birth", "gender"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone Number"
        self.fields["gender"].widget.attrs["placeholder"] = "Gender"
        self.fields["birth"].widget.attrs["placeholder"] = "Birth Day"
        

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["country","state","city","street","zip_code"]

    def __init__(self, *args, **kwargs):
        super(AddressForm,self).__init__(*args, **kwargs)
        self.fields["country"].widget.attrs["placeholder"] = "Country"
        self.fields["state"].widget.attrs["placeholder"] = "State"
        self.fields["city"].widget.attrs["placeholder"] = "City"
        self.fields["street"].widget.attrs["placeholder"] = "Street"
        self.fields["zip_code"].widget.attrs["placeholder"] = "Zip Code"
