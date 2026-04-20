from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # This dictates which columns show up in the admin list view
    list_display = ('company_name', 'contact_person', 'email', 'is_active')
    search_fields = ('company_name', 'contact_person')
    list_filter = ('is_active',)