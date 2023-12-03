from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['thumbnail', 'shortDescription', 'slk','slb','gianhap','giaban','category','slkbd']
