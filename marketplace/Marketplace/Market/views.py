from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *
from django.urls import reverse

# Create your views here.


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Redirect to a page showing the list of products
    else:
        form = ProductForm()
    return render(request, 'template/market/create_product.html', {'form': form})

def home(request):
    products = Product.objects.all()
    cart = Cart.objects.all()




    return render(request, 'template/market/home.html', {'products': products, 'cart': cart, 'all': all})


def about(request):
    return render(request, 'template/market/view.html')
