from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from json import load

from django.conf import settings
from django.core.cache import cache


from django.views.generic import DetailView

from .models import ProductCategory, Product

# Create your views here.


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()


def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)


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
    # context['categories'] = ProductCategory.objects.all()
    context['categories'] = get_link_category()
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
