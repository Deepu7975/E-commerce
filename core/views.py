from django.shortcuts import render, redirect
from .forms import ProductForm, ProductVarientForm, ProductImageForm
from .models import Product, ProductVarient, ProductImage
from django.contrib.auth.decorators import login_required


@login_required(login_url='/sellar/sellar_signin/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            # auto-link to the logged-in seller
            if hasattr(request.user, 'seller_profile'):
                product.seller = request.user.seller_profile
            product.save()
            return redirect('display_products')
    context = {'form': ProductForm()}
    return render(request, 'add_product.html', context)


@login_required(login_url='/sellar/sellar_signin/')
def product_varient(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductVarientForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.product = product       # ✅ fixed: set product manually
            variant.save()
            return redirect('varients', product_id=product.id)
    pro_var = ProductVarient(product=product)
    context = {'form': ProductVarientForm(instance=pro_var), 'product': product}
    return render(request, 'product_varient.html', context)


@login_required(login_url='/sellar/sellar_signin/')
def product_image(request):
    if request.method == 'POST' and request.FILES:
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_products')
    context = {'form': ProductImageForm()}
    return render(request, 'product_image.html', context)


@login_required(login_url='/sellar/sellar_signin/')
def display_products(request):
    # show only the logged-in seller's products
    if hasattr(request.user, 'seller_profile'):
        products = Product.objects.filter(seller=request.user.seller_profile)
    else:
        products = Product.objects.all()
    context = {'products': products}
    return render(request, 'display_products.html', context)


@login_required(login_url='/sellar/sellar_signin/')
def display_varients(request, product_id):
    pro = Product.objects.get(id=product_id)
    qs = ProductVarient.objects.filter(product=pro)
    return render(request, 'display_varients.html', {'varients': qs, 'product': pro})


@login_required(login_url='/sellar/sellar_signin/')
def add_image(request, varient_id):
    varient = ProductVarient.objects.get(id=varient_id)
    pro = varient.product
    if request.method == 'POST' and request.FILES:
        fm = ProductImageForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('varients', product_id=pro.id)
    pro_image = ProductImage(product=pro, varient=varient)
    fm = ProductImageForm(instance=pro_image)
    context = {'form': fm, 'varient': varient, 'product': pro}
    return render(request, 'add_image.html', context)


def product_list(request):
    qs = ProductImage.objects.filter(is_primary=True)
    context = {'products': qs}
    return render(request, 'home.html', context)
