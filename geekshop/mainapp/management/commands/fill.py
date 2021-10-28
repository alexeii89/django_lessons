from django.core.management.base import BaseCommand
import json
from django.conf import settings

from authapp.models import ShopUser

from mainapp.models import Product, ProductCategory


def load_from_json(filename):
    with open(f'{settings.BASE_DIR}/json/{filename}.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

        categoryes = load_from_json('categoryes')

        for category in categoryes:
            ProductCategory.objects.create(**category)

        products = load_from_json('products')

        for product in products:
            product['category'] = ProductCategory.objects.get(
                name=product['category'])
            Product.objects.create(**product)

        ShopUser.objects.create_superuser(
            username='django', password='geekbreins')
