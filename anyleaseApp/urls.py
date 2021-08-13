from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import ListCategory, DetailCategory, ListProduct, DetailProduct, ListUser, DetailUser

urlpatterns = [
    path('categories', ListCategory.as_view(), name = 'categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name = 'category'),
    path('products', ListProduct.as_view(), name = 'products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name = 'product'),
    path('users', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='user')
]
