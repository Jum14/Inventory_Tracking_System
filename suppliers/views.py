from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Supplier
from .forms import SupplierForm

@login_required
@permission_required('suppliers.view_supplier', raise_exception=True)
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'suppliers/supplier_list.html', context)

@login_required
@permission_required('suppliers.add_supplier', raise_exception=True)
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    
    context = {'form': form, 'action': 'Create'}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required
@permission_required('suppliers.change_supplier', raise_exception=True)
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    
    context = {'form': form, 'action': 'Edit'}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required
@permission_required('suppliers.delete_supplier', raise_exception=True)
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    
    context = {'supplier': supplier}
    return render(request, 'suppliers/supplier_confirm_delete.html', context)

@login_required
@permission_required('suppliers.view_supplier', raise_exception=True)
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})