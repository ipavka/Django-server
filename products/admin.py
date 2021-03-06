from django.contrib import admin

from django.contrib import admin
from products.models import Product, ProductCategory


# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'price', 'quantity', 'category')
    ordering = ('-name',)
    search_fields = ('name',)
