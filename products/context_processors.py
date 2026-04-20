from .models import Product

def low_stock_alerts(request):
    if request.user.is_authenticated:
        # Get all products where stock is below or equal to min level
        low_stock_products = [p for p in Product.objects.all() if p.is_low_stock()]
        return {
            'low_stock_count': len(low_stock_products),
            'low_stock_items': low_stock_products[:5] # Show only top 5 in dropdown
        }
    return {}