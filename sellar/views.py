from django.shortcuts import render,redirect
from account.models import User
from .forms import SellarRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def sellar_register_view(request):
    if request.method=='POST':
        fm =SellarRegistrationForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Sellar Account created successfully')
            return redirect('sellar_signin')
        context={"form":fm}
        return render(request,'sellar/sellar_register.html',context)
    context={
        "form":SellarRegistrationForm()
        }
    return render(request,'sellar/sellar_register.html',context)

def sellar_signin_view(request):
    if request.method=='POST':
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    if user.role=='seller':
                        return redirect('display_products')
        context={"form":fm}
        return render(request,'sellar/sellar_signin.html',context)
    context={"form":AuthenticationForm()}
    return render(request,'sellar/sellar_signin.html',context)

            