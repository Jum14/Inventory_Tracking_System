import json # Add this at the top
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from suppliers.models import Supplier
from .models import Product, Category 
from .forms import ProductForm, ProductStockUpdateForm

from django.db.models import Sum # Add this too

@login_required
def dashboard_view(request):
    from transactions.models import Transaction
    
    # Existing counts
    products = Product.objects.all()
    categories = Category.objects.annotate(total_stock=Sum('products__current_stock'))
    
    # Prepare data for Pie Chart (Category Names and Stock Totals)
    category_labels = [c.name for c in categories]
    category_data = [c.total_stock or 0 for c in categories]

    # Prepare data for Bar Chart (Top 5 Products Stock vs Min Level)
    top_products = products.order_by('current_stock')[:5]
    product_labels = [p.name for p in top_products]
    product_stock = [p.current_stock for p in top_products]
    product_min = [p.min_stock_level for p in top_products]

    context = {
        'total_users': User.objects.count(),
        'total_products': products.count(),
        'total_suppliers': Supplier.objects.count(),
        'total_categories': categories.count(), 
        'products': products.order_by('-id')[:10],
        
        # Chart Data (Converted to JSON for JS to read)
        'category_labels': json.dumps(category_labels),
        'category_data': json.dumps(category_data),
        'product_labels': json.dumps(product_labels),
        'product_stock': json.dumps(product_stock),
        'product_min': json.dumps(product_min),
    }
    return render(request, 'dashboard.html', context)

@login_required
def category_list(request):
    categories = Category.objects.all().prefetch_related('products')
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)

@login_required
@permission_required('products.view_product', raise_exception=True)
def product_list(request):
    products = Product.objects.select_related('category', 'supplier').all()
    categories = Category.objects.all()

    # Dynamic Filtering Logic
    cat_id = request.GET.get('category')
    search_q = request.GET.get('search')
    sort_by = request.GET.get('sort', '-date_added')

    if cat_id and cat_id != 'all':
        products = products.filter(category_id=cat_id)
    if search_q:
        products = products.filter(name__icontains=search_q) | products.filter(sku__icontains=search_q)
    
    products = products.order_by(sort_by)

    context = {
        'products': products,
        'categories': categories,
    }

    # If request comes from HTMX, return only the partial table
    if request.headers.get('HX-Request'):
        return render(request, 'products/partials/product_table.html', context)
    
    return render(request, 'products/product_list.html', context)

@login_required
@permission_required('products.add_product', raise_exception=True)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'action': 'Create'})

@login_required
@permission_required('products.change_product', raise_exception=True)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    old_stock = product.current_stock
    FormClass = ProductForm if request.user.is_superuser else ProductStockUpdateForm
    
    if request.method == 'POST':
        form = FormClass(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            new_stock = product.current_stock
            if old_stock != new_stock:
                from transactions.models import Transaction
                diff = new_stock - old_stock
                Transaction.objects.create(
                    product=product,
                    transaction_type='IN' if diff > 0 else 'OUT',
                    quantity=abs(diff),
                    status='COMPLETED',
                    handled_by=request.user,
                    remarks=f"Manual adjustment: {old_stock} → {new_stock}."
                )
            return redirect('product_list')
    else:
        form = FormClass(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'action': 'Edit', 'product': product})

@login_required
@permission_required('products.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

@login_required
@permission_required('products.view_product', raise_exception=True)
def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related('category', 'supplier'), pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})