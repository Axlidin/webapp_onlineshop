from .models import Product, Category
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', "category", "productname", "price"]
    list_filter = ['category', "productname"]
    search_fields = ['category', "productname"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', "name"]
