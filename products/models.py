from django.db import models
from suppliers.models import Supplier

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Fields for UI Customization
    icon = models.CharField(max_length=50, default="bi-tag", help_text="Bootstrap icon class (e.g., bi-laptop)")
    color_theme = models.CharField(max_length=20, default="success", help_text="Bootstrap color (success, info, warning, primary)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU")
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='products'
    )
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_stock = models.IntegerField(default=0)
    min_stock_level = models.IntegerField(default=5) # New threshold field
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateTimeField(auto_now_add=True)

    def is_low_stock(self):
        return self.current_stock <= self.min_stock_level

    def __str__(self):
        return f"{self.sku} - {self.name}"