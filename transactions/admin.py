from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'transaction_type', 'quantity', 'timestamp')
    list_filter = ('transaction_type', 'timestamp')
    search_fields = ('product__name', 'remarks')