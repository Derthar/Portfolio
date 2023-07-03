from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from Products.models import Product, ProductCategory, Basket
from django.core.paginator import Paginator
from Users.models import User

# Create your views here.

def index(request):
    context = {
        'title': 'Test title',
        'username': 'Buffalo',
        'is_promotion': True,
    }
    return render(request, 'Products/index.html', context = context)

def products(request, category_id = None, page_number = 1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Store Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'Products/products.html', context=context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if baskets.exists():
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])