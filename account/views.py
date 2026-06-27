from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def registerview(request):
    if request.method == 'POST':
        fm = RegistrationForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created successfully')
            return redirect('signin')
        context = {"form": fm}
        return render(request, 'register.html', context)
    context = {"form": RegistrationForm()}
    return render(request, 'register.html', context)


def signinview(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_authenticated:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                if user.role == 'seller':
                    return redirect('display_products')
                elif user.is_staff or user.role == 'admin':
                    return redirect('/admin/')
                else:
                    return redirect('home')     # customer
            else:
                messages.error(request, 'Invalid username or password.')
        context = {"form": fm}
        return render(request, 'signin.html', context)
    context = {"form": AuthenticationForm()}
    return render(request, 'signin.html', context)


def logoutview(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('signin')
