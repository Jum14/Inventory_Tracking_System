from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Added 'icon' and 'color_theme' so you can see/edit them in the list
    list_display = ('name', 'icon', 'color_theme', 'description')
    search_fields = ('name',)
    # This makes it easy to quickly edit the look of categories
    list_editable = ('icon', 'color_theme') 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'supplier', 'current_stock', 'unit_price')
    search_fields = ('name', 'sku')
    list_filter = ('category', 'supplier')