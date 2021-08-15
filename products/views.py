from django.shortcuts import render
import json


# не знаю как верно, тут оставить или в функции разместить
with open('./products/fixtures/goods.json', 'r', encoding='utf-8') as file:
    data_prod = json.load(file)


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': data_prod
    }
    return render(request, 'products/products.html', context)


# def products(request):
#     context = {
#         'title': 'GeekShop - Каталог',
#         'header': 'Добро пожаловать на сайт!',
#         'username': 'Иван Иванов',
#         'products': data_prod
#     }
#     return render(request, 'products/products.html', context)
