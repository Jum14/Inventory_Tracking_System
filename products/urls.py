from django.urls import path
from . import views

urlpatterns = [
    # The New Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # NEW: The Categories List (Accessible by Admin and Staff)
    path('categories/', views.category_list, name='category_list'),

    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]