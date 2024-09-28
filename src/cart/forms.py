from typing import Any
from django import forms
from .models import Category, Product,Discount
from website.views import NavbarUserTypeMixin


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "price", "image", "category"]

        def __init__(self, *args, **kwargs):
            super(AddProductForm, self).__init__(*args, **kwargs)
            self.fields["name"].widget.attrs["placeholder"] = "Product Name"
            self.fields["price"].widget.attrs["placeholder"] = "Price"


class DiscountType(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ["category","product"]
    TYPES = ((1, "$"), (2, "%"))
    type_discount = forms.ChoiceField(choices=TYPES)
    number = forms.IntegerField()


class DiscountProductForm(DiscountType):
    pass

class DiscountCategoryForm(DiscountType):
    pass


