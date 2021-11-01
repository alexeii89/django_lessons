from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from random import random, shuffle
from basketapp.models import Basket

# Create your views here.


def index(request):
    context = {
        'title': 'главная',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk).order_by('price')

    basket = []
    sum_basket = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for i in basket:
            sum_basket = sum_basket + i.quantity

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
            'sum_basket': sum_basket
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = list(Product.objects.all().order_by('pk')[:10])
    shuffle(same_products)
    print(same_products)
    context = {
        'title': title,
        'links_menu': links_menu,
        'first_same_products': same_products[0],
        'same_products': same_products[1:4]
    }

    return render(request, 'mainapp/products.html', context)
