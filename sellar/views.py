from django.shortcuts import render, redirect
from account.models import User
from .forms import SellarRegistrationForm, SellerProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def sellar_register_view(request):
    if request.method == 'POST':
        fm = SellarRegistrationForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Seller account created! Please sign in.')
            return redirect('sellar_signin')
        context = {"form": fm}
        return render(request, 'sellar/sellar_register.html', context)
    context = {"form": SellarRegistrationForm()}
    return render(request, 'sellar/sellar_register.html', context)


def sellar_signin_view(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_authenticated:
                login(request, user)
                messages.success(request, 'Welcome back!')
                if user.role == 'seller':
                    return redirect('display_products')
                else:
                    return redirect('home')     # ✅ fixed: no longer stuck
            else:
                messages.error(request, 'Invalid username or password.')
        context = {"form": fm}
        return render(request, 'sellar/sellar_signin.html', context)
    context = {"form": AuthenticationForm()}
    return render(request, 'sellar/sellar_signin.html', context)


def sellar_logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('sellar_signin')

@login_required(login_url='/sellar/sellar_signin/')
def seller_profile_view(request):
    # ✅ Guard: only sellers have a seller_profile
    if not hasattr(request.user, 'seller_profile'):
        messages.error(request, 'You do not have a seller account.')
        return redirect('home')

    seller = request.user.seller_profile
    if request.method == 'POST':
        form = SellerProfileForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            messages.success(request, 'Store profile updated successfully!')
            return redirect('display_products')
    else:
        form = SellerProfileForm(instance=seller)
    return render(request, 'sellar/seller_profile.html', {'form': form, 'seller': seller})