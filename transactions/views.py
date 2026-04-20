from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Transaction
from .forms import TransactionForm

# REMOVED: 'from products.models import Product' from here to prevent crashes!

@login_required
@permission_required('transactions.view_transaction', raise_exception=True)
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-timestamp')
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

@login_required
@permission_required('transactions.add_transaction', raise_exception=True)
def transaction_create(request):
    # LOCAL IMPORT: This is the fix. 
    # It only loads Product when the button is actually clicked.
    from products.models import Product 

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # 1. Save the transaction record (but don't commit yet to set the user)
            transaction = form.save(commit=False)
            transaction.handled_by = request.user
            
            # 2. Get the product involved
            product = transaction.product
            
            # 3. Adjust the stock math
            if transaction.transaction_type == 'IN':
                product.current_stock += transaction.quantity
            elif transaction.transaction_type == 'OUT':
                product.current_stock -= transaction.quantity
            
            # 4. Save both the updated product and the transaction
            product.save()
            transaction.save()
            
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    
    context = {
        'form': form,
        'action': 'Record'
    }
    return render(request, 'transactions/transaction_form.html', context)