from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryRegisterForm, ProductRegisterForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


# Users
class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Регистрация'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Обновление'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Удаление'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


# Categories
class ProductCategoriesListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesListView, self).dispatch(request, *args, **kwargs)


class ProductCategoriesCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-create.html'
    form_class = ProductCategoryRegisterForm
    success_url = reverse_lazy('admins:admin_product_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Заведение категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesCreateView, self).dispatch(request, *args, **kwargs)


class ProductCategoriesUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-update-delete.html'
    form_class = ProductCategoryRegisterForm
    success_url = reverse_lazy('admins:admin_product_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Обновление'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesUpdateView, self).dispatch(request, *args, **kwargs)


class ProductCategoriesDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-product-categories-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_product_categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Удаление'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoriesDeleteView, self).dispatch(request, *args, **kwargs)


# Products
class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)


class ProductsCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductRegisterForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Заведение продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsCreateView, self).dispatch(request, *args, **kwargs)


class ProductsUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductRegisterForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Обновление'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsUpdateView, self).dispatch(request, *args, **kwargs)


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Удаление'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsDeleteView, self).dispatch(request, *args, **kwargs)

