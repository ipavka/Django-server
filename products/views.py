from django.shortcuts import render
import json
from datetime import datetime

# не знаю как верно, тут оставить или в функции разместить
with open('./products/fixtures/products.json', 'r', encoding='utf-8') as file:
    data_prod = json.load(file)


def index(request):
    context = {
        "title": "geekShop"
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'geekShop - Каталог',
        "date": datetime.now(),
        'products': data_prod
    }
    return render(request, 'products/products.html', context)

