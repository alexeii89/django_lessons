from django.shortcuts import render
from mainapp.models import Product
# Create your views here.


def index(request):
    context = {
        'title': 'главная',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


links_menu = [
    {'url': 'products', 'title_name': 'Все'},
    {'url': 'products_home', 'title_name': 'Дом'},
    {'url': 'products_office', 'title_name': 'Офис'},
    {'url': 'products_modern', 'title_name': 'Модерн'},
    {'url': 'products_classic', 'title_name': 'Классика'}
]


def contact(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    context = {
        'links_menu': links_menu,
        'title': 'все продукты'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты для дома'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты для офиса'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты модерн'
    }
    return render(request, 'mainapp/products.html', context=context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты классика'
    }
    return render(request, 'mainapp/products.html', context=context)
