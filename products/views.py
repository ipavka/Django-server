from django.shortcuts import render
import json


def index(request):
    return render(request, 'products/index.html')


def products(request):
    with open('./products/fixtures/goods.json', 'r', encoding='utf-8') as file:
        data_prod = json.load(file)
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': data_prod
    }
    return render(request, 'products/products.html', context)
