from django.urls import path
from .import views

urlpatterns = [
    path('product-details/<slug:slug>', views.product_details, name='product_details'),
]