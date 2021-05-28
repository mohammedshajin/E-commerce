from .models import Product
from django.shortcuts import render

def product_details(request, slug):
    product = Product.objects.get(slug=slug)

    return render(request, 'product_details.html', {'product':product})