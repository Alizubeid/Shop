from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "price", "image", "category"]

        def __init__(self, *args, **kwargs):
            super(AddProductForm, self).__init__(*args, **kwargs)
            self.fields["name"].widget.attrs["placeholder"] = "Product Name"
            self.fields["price"].widget.attrs["placeholder"] = "Price"
