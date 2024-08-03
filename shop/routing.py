from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', product_catalog, name='product_catalog'),
    path('detail/<int:id>/', product_detail, name='product_detail'),
    path('suppliers/', suppliers, name='suppliers'),
    path('supplier/<int:supplier_id>/', supplier_detail, name='supplier_detail'),
    path('add_supplier/', add_supplier, name='add_supplier'),
]