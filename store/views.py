from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')


def products(request):
    products = Product.objects.all()
    return render(request,'products.html',{'products':products})


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    print(product, product_id)
    return render(request,'product.html',{'product':product})
