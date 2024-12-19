from django.shortcuts import render
from .models import Product

# Create your views here.

def product (request):
    return render(request, 'product/product.html')
def products (request):
    return render(request, 'products/products.html',{'pro': Product.objects.all()})
