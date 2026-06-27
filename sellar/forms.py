from django import forms
from account.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Seller


class SellarRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'seller'
        if commit:
            user.save()
            # ensure a Seller profile exists for this user
            Seller.objects.get_or_create(user=user)
        return user
# ===================================================
# sellar/forms.py  — ADD SellerProfileForm below the existing form
# ===================================================

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


# ✅ NEW: Seller profile completion form
class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'store_name',
            'store_description',
            'business_type',
            'gst_number',
            'address',
            'city',
            'state',
            'country',
            'pincode',
            'phone',
        ]
        widgets = {
            'store_description': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }


# ===================================================
# sellar/views.py  — ADD seller_profile_view below existing views
# ===================================================

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import SellarRegistrationForm, SellerProfileForm
# from .models import Seller

"""
Add this import at the top of sellar/views.py:
    from .forms import SellarRegistrationForm, SellerProfileForm
    from django.contrib.auth.decorators import login_required

Then add this view:
"""

# @login_required(login_url='/sellar/sellar_signin/')
# def seller_profile_view(request):
#     seller = request.user.seller_profile   # OneToOne from Seller model
#     if request.method == 'POST':
#         form = SellerProfileForm(request.POST, instance=seller)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Store profile updated successfully!')
#             return redirect('display_products')
#     else:
#         form = SellerProfileForm(instance=seller)
#     return render(request, 'sellar/seller_profile.html', {'form': form, 'seller': seller})


# ===================================================
# sellar/urls.py  — ADD the profile URL
# ===================================================

# urlpatterns = [
#     path('sellar_register/', views.sellar_register_view, name='sellar_register'),
#     path('sellar_signin/',   views.sellar_signin_view,   name='sellar_signin'),
#     path('profile/',         views.seller_profile_view,  name='seller_profile'),  # ✅ NEW
# ]