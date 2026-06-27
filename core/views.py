from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='seller/sellar_sigin/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_products') 
    context={
        'form':ProductForm()
    }
    return render(request,'add_product.html',context)
# Change ALL @login_required decorators to:
@login_required(login_url='/sellar/sellar_signin/')

# Fix product_varient view:
def product_varient(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductVarientForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.product = product          # ← set product manually
            variant.save()
            return redirect(f'/core/display_varients/{product.id}/')
    pro_var = ProductVarient(product=product)
    context = {'form': ProductVarientForm(instance=pro_var)}
    return render(request, 'product_varient.html', context)

@login_required(login_url='seller/sellar_sigin/')
def product_image(request):

    if request.method == 'POST' and request.FILES:
        form =ProductImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_products') 
    context={
        'form':ProductImageForm()
    }
    return render(request,'product_image.html',context)


@login_required(login_url='seller/sellar_sigin/')
def display_products(request):
    context = {
        'products': Product.objects.all(),
        'images': ProductImage.objects.all(),
        'variants': ProductVarient.objects.all(),
    }
    return render(request, 'display_products.html', context)

@login_required(login_url='seller/sellar_sigin/')
def display_varients(request,product_id):
    pro = Product.objects.get(id=product_id)
    qs = ProductVarient.objects.filter(product = pro)
    return render(request,'display_varients.html',{'varients':qs,'product':pro})

@login_required(login_url='seller/sellar_sigin/')
def add_image(request,varient_id):
    varient = ProductVarient.objects.get(id=varient_id)
    pro = varient.product
    if request.method == 'POST' and request.FILES:
        fm = ProductImageForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect(f'/display_varients/{pro.id}')

    pro_image = ProductImage(product=pro,varient=varient)
    fm = ProductImageForm(instance=pro_image)
    context = {
        'form':fm
    }
    return render(request,'add_image.html',context)



def product_list(request):
    qs=ProductImage.objects.filter(is_primary=True)
    context = {
        'products': qs
    }
    return render(request, 'home.html', context)