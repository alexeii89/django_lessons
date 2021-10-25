from django.shortcuts import render
from mainapp.models import Product, ProductCategory
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
    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'все продукты'
    }
    return render(request, 'mainapp/products.html', context=context)
