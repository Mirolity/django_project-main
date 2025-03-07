from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
]
