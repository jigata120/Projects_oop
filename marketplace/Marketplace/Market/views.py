from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import *
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'template/market/edit_product.html', {'form': form, "product": product})


def delete_product_from_cart(request, product_id):
    cart1 = get_object_or_404(Cart, buyer=request.user)
    cart = cart1.products
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('home')


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('home')


def add_to_cart(request, product_id):
    # Logic to add product to cart
    cart1 = get_object_or_404(Cart, buyer=request.user)
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

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():

            product = form.save(commit=False)
            product.seller = request.user  # Set the seller to the logged-in user
            product.save()
            return redirect(reverse('home'))  # Redirect to a page showing the list of products
    else:
        form = ProductForm()
    return render(request, 'template/market/create_product.html', {'form': form})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'template/market/product_details.html', {'product': product})

@login_required
def home(request):
    products = Product.objects.all()
    cart = get_object_or_404(Cart, buyer=request.user)
    cart = cart.products.all()
    total_price = cart_price(cart)
    return render(request, 'template/market/home.html',
                  {'products': products, 'cart': cart, 'total_price': total_price,"current_user" : request.user})


def about(request):
    return render(request, 'template/market/view.html')
