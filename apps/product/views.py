from .models import Product
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddToCartForm
from apps.cart.cart import Cart

def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')
            return redirect('product_details.html', slug=slug)
    else:
        form = AddToCartForm()


    return render(request, 'product_details.html', {'product':product})