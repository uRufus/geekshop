from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from json import load

from django.views.generic import DetailView

from .models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):
    context = {
        'title': 'geekshop - каталог',
    }
    if id_category:
        product = Product.objects.filter(category_id=id_category).select_related('category')
    else:
        product = Product.objects.all().select_related('category')

    paginator = Paginator(product, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()
    context['vendor_slides'] = load(open('mainapp/fixtures/vendor_slides.json', encoding='utf-8'))
    # content = load(open('mainapp/fixtures/products.json', encoding='utf-8'))
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'
    # context_object_name = 'product'


    def get_context_data(self, **kwargs):
        """ Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
