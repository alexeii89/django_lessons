from django.contrib import admin
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser

admin.site.register(ShopUser)
admin.site.register(Product)
admin.site.register(ProductCategory)

# Register your models here.
