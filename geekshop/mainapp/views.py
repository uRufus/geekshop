from django.shortcuts import render
from json import load
from .models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekshop - каталог',
    }
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    context['vendor_slides'] = load(open('mainapp/fixtures/vendor_slides.json', encoding='utf-8'))
    # content = load(open('mainapp/fixtures/products.json', encoding='utf-8'))
    return render(request, 'mainapp/products.html', context)
