from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import *
from django.urls import reverse


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Redirect to a page showing the list of products
    else:
        form = ProductForm()
    return render(request, 'template/market/create_product.html', {'form': form})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'template/market/product_details.html', {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, 'template/market/home.html', {'products': products, })


def about(request):
    return render(request, 'template/market/view.html')
