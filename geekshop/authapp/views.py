from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from baskets.models import Basket
from django.shortcuts import render, get_object_or_404

from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin


class UserLoginView(LoginView, BaseClassContextMixin):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    title = 'geekshop - авторизация'


class UserRegisterView(CreateView, BaseClassContextMixin):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:login')
    title = 'geekshop - регистрация'


class UserProfileView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp/profile.html')

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['title'] = 'geekshop - профайл'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class UserLogoutView(LogoutView):
    template_name = 'mainapp/index.html'

