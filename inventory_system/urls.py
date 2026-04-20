from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Django's built-in authentication URLs (Added for Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # We will hook up the apps here:
    path('products/', include('products.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('transactions/', include('transactions.urls')),
]