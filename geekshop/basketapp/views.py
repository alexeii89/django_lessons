from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = 'Карзина'
    basket = []
    total_sum = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for i in basket:
            total_sum += i.quantity * i.product.price

    content = {
        'title': title,
        'basket': basket,
        'total_sum': total_sum
    }
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)
