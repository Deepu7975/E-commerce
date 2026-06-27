from django import forms
from account.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Seller


class SellarRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'seller'
        if commit:
            user.save()
            Seller.objects.get_or_create(user=user)
        return user


class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'store_name', 'store_description', 'business_type',
            'gst_number', 'address', 'city', 'state',
            'country', 'pincode', 'phone',
        ]
        widgets = {
            'store_description': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }
