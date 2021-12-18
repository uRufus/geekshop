from django.urls import path

from admins.views import index, UserCreateView, UserUpdateView, UserDeleteView, \
    UserListView, ProductCategoriesListView, ProductCategoriesCreateView, \
    ProductCategoriesUpdateView, ProductCategoriesDeleteView, ProductsListView, ProductsCreateView, \
    ProductsUpdateView, ProductsDeleteView

app_name = 'admins'




urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('product-categories/', ProductCategoriesListView.as_view(), name='admin_product_categories'),
    path('product-categories-create/', ProductCategoriesCreateView.as_view(), name='admin_product_categories_create'),
    path('product-categories-update/<int:pk>', ProductCategoriesUpdateView.as_view(), name='admin_product_categories_update'),
    path('product-categories-delete/<int:pk>', ProductCategoriesDeleteView.as_view(), name='admin_product_categories_delete'),
    path('products/', ProductsListView.as_view(), name='admin_products'),
    path('products-create/', ProductsCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', ProductsUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>', ProductsDeleteView.as_view(), name='admin_products_delete'),
]
