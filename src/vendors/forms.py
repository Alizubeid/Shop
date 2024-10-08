from django import forms
from accounts.models import User
from vendors.models import Company, Owner, Manager, Operator
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ProfileForm,AddressForm



class OwnerCreationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = ["email"]
    
    def __init__(self, *args, **kwargs):
        super(OwnerCreationForm,self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["company_name",]
    
    def __init__(self, *args, **kwargs):
        super(CompanyCreationForm,self).__init__(*args, **kwargs)
        self.fields["company_name"].widget.attrs["placeholder"] = "Company Name"

class StaffCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email"]
    
    def __init__(self, *args, **kwargs):
        super(StaffCreationForm,self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"