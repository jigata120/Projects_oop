from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import *
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def filter_products_by_price(request):
    min_price = request.GET.get('min_price')  # Get min_price from user input
    max_price = request.GET.get('max_price')  # Get max_price from user input
    cart = get_object_or_404(Cart, buyer=request.user)
    cart = cart.products.all()
    total_price = cart_price(cart)
    if not min_price and not max_price:
        # If both are empty, render the home page with no filters
        products_in_price_range = Product.objects.all()
        return redirect('home')
    elif not min_price or not max_price:
        if not min_price:
            min_price = 0
        else:
            max_price = 10000

    # Filter products by price range
    products_in_price_range = Product.objects.filter(price__gte=min_price, price__lte=max_price)
    # Handle the case where the input is not a valid decimal

    return render(request, 'template/market/home.html',
                  {'products': products_in_price_range, 'cart': cart, 'total_price': total_price,
                   "current_user": request.user})


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
    product.quantity += 1
    product.save()
    cart.remove(product)
    return redirect('home')


def custom_404_view(request, exception):
    return render(request, 'custom_404.html', status=404)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('home')


def add_to_cart(request, product_id):
    # Logic to add product to cart
    cart1 = get_object_or_404(Cart, buyer=request.user)
    cart = cart1.products
    product = get_object_or_404(Product, pk=product_id)
    product.quantity -= 1
    product.save()
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
            product.seller = request.user
            if product.is_valid_product():  # Set the seller to the logged-in user
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
                  {'products': products, 'cart': cart, 'total_price': total_price, "current_user": request.user})


def about(request):
    return render(request, 'template/market/view.html')
