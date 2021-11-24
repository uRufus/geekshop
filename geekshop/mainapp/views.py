from django.shortcuts import render
from json import load
from .models import ProductCategory, Product

# Create your views here.


def index(request):
    content = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'geekshop - каталог',
    }
    content['products'] = Product.objects.all()
    content['vendor_slides'] = load(open('mainapp/fixtures/vendor_slides.json', encoding='utf-8'))
    # content = load(open('mainapp/fixtures/products.json', encoding='utf-8'))
    return render(request, 'mainapp/products.html', content)
