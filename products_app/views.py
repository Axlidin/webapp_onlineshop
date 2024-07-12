from django.shortcuts import render
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'info/category.html', {'categories': categories})

def product_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'info/product.html', {'products': products})

def cart(request):
    # Add your cart logic here
    return render(request, 'info/cart.html')

def promotions(request):
    # Add your promotions logic here
    return render(request, 'info/promotions.html')
