from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryRegisterForm, ProductRegisterForm
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import ProductCategory, Product


class IndexTemplateView(TemplateView, CustomDispatchMixin):
    template_name = 'admins/admin.html'


# Users
class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Geekshop - Админ | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Geekshop - Админ | Регистрация'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Geekshop - Админ | Обновление'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Geekshop - Админ | Удаление'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Categories
class ProductCategoriesListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-read.html'
    title = 'Geekshop - Админ | Категории'


class ProductCategoriesCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-create.html'
    form_class = ProductCategoryRegisterForm
    success_url = reverse_lazy('admins:admin_product_categories')
    title = 'Geekshop - Админ | Заведение категории'


class ProductCategoriesUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-update-delete.html'
    form_class = ProductCategoryRegisterForm
    success_url = reverse_lazy('admins:admin_product_categories')
    title = 'Geekshop - Админ | Обновление'


class ProductCategoriesDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_product_categories')
    title = 'Geekshop - Админ | Удаление'


# Products
class ProductsListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Geekshop - Админ | Продукты'


class ProductsCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductRegisterForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Geekshop - Админ | Заведение продукта'


class ProductsUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductRegisterForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Geekshop - Админ | Обновление'


class ProductsDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Geekshop - Админ | Удаление'


