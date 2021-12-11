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


def products(request):
    context = {
        'title': 'geekshop - каталог',
    }
    context['products'] = Product.objects.all()
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
