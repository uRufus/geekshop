import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import User


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategory.objects.get(id=category)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()

        users = load_from_json('authapp/fixtures/users.json')

        User.objects.all().delete()
        for user in users:
            usr = user.get('fields')
            usr['id'] = user.get('pk')
            new_user = User(**usr)
            new_user.save()

