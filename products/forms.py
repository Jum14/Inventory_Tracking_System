from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Added 'category' to the fields list
        fields = ['name', 'sku', 'category', 'description', 'unit_price', 'current_stock', 'supplier']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU-001'}),
            # Added form-select for the dropdown menu
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'current_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-select'}),
        }

class ProductStockUpdateForm(forms.ModelForm):
    """
    Limited form used by staff (like John Doe) to only modify 
    inventory levels without changing product metadata.
    """
    class Meta:
        model = Product
        fields = ['current_stock']
        widgets = {
            'current_stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }