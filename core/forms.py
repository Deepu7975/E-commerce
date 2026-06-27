from django import forms
from .models import Product, ProductVarient, ProductImage, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductVarientForm(forms.ModelForm):
    class Meta:
        model = ProductVarient
        # product will be set by the view; exclude it from the form
        exclude = ['product']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model =ProductImage
        fields= '__all__' 


