from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),

    path('categories/<int:category_id>/products/', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('promotions/', views.promotions, name='promotions'),
]
