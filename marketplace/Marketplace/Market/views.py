from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import *
from django.urls import reverse
from django.http import HttpResponse


def delete_product(request, product_id):
    cart = Cart.objects.all()
    cart1 = cart.first()
    cart = cart1.products
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('home')


def add_to_cart(request, product_id):
    # Logic to add product to cart
    cart = Cart.objects.all()
    cart1 = cart.first()
    cart = cart1.products
    product = get_object_or_404(Product, pk=product_id)
    cart.add(product)
    cart1.save()
    return redirect('home')


def cart_price(cart_objects):
    final_price = 0
    for product in cart_objects:
        final_price += product.price
    return final_price


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
    cart = Cart.objects.all()
    cart = cart.first()
    cart = cart.products.all()
    total_price = cart_price(cart)
    return render(request, 'template/market/home.html',
                  {'products': products, 'cart': cart, 'total_price': total_price})


def about(request):
    return render(request, 'template/market/view.html')
