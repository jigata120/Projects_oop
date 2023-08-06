from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    cart = Cart.objects.all()




    return render(request, 'template/market/home.html', {'products': products, 'cart': cart, 'all': all})


def about(request):
    return render(request, 'template/market/view.html')
