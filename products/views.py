from django.shortcuts import render
from datetime import datetime
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        "title": "geekShop"
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'geekShop - Каталог',
        "date": datetime.now(),
        'categories': ProductCategory.objects.all(),
    }
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(product, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator

    return render(request, 'products/products.html', context)

