from django.shortcuts import render
from apps.product.models import Product

def home(request):
    product = Product.objects.all()
    return render (request, 'home.html', {'product':product})

# Create your views here.
