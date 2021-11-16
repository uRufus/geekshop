from django.shortcuts import render
from json import load


# Create your views here.


def index(request):
    content = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = load(open('mainapp/fixtures/products.json', encoding='utf-8'))
    return render(request, 'mainapp/products.html', content)
