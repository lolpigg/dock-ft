from django.contrib import admin
from .models import *

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'discount')
    list_display_links = ('order', 'product')
    list_filter = ('order', 'product')
    search_fields = ('order__order_number', 'product__name')
    list_editable = ('quantity', 'discount')
    ordering = ('order',)

@admin.register(DeliveryItem)
class DeliveryItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'delivery', 'quantity')
    list_display_links = ('product', 'delivery')
    list_filter = ('product', 'delivery')
    search_fields = ('product__name', 'delivery__delivery_number')
    list_editable = ('quantity',)
    ordering = ('delivery',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery_number', 'delivery_date', 'supplier')
    list_display_links = ('delivery_number',)
    list_filter = ('supplier', 'delivery_date')
    search_fields = ('delivery_number', 'supplier__name')
    ordering = ('delivery_date',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'comment', 'delivery_address', 'delivery_method', 'created_date', 'completion_date')
    list_display_links = ('order_number',)
    list_filter = ('delivery_method', 'created_date')
    search_fields = ('order_number', 'customer_name')
    ordering = ('-created_date',)  # Минус обозначает сортировку по убыванию

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)  # Поля для перехода при клике в списке записей
    list_filter = ('name',)  # Поля для фильтрации в админке
    search_fields = ('name', 'description')  # Поля для поиска
    list_editable = ('description',)  # Изменяемые поля
    ordering = ('name',)  # Поля для сортировки

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')
    list_editable = ('description',)
    ordering = ('name',)

@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('product', 'characteristic', 'value')
    list_display_links = ('product',)  # Поля для перехода при клике в списке записей
    list_filter = ('product', 'characteristic')  # Поля для фильтрации в админке
    search_fields = ('product__name', 'characteristic', 'value')  # Поля для поиска
    list_editable = ('value',)  # Изменяемые поля
    ordering = ('product',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_date', 'updated_date', 'is_deleted')
    list_display_links = ('name',)
    list_filter = ('category', 'created_date', 'is_deleted')
    search_fields = ('name', 'price')
    list_editable = ('is_deleted',)
    ordering = ('-created_date',)  # Минус обозначает сортировку по убыванию

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'representative_name', 'representative_phone', 'address', 'is_deleted')
    list_display_links = ('company_name',)
    list_filter = ('company_name', 'representative_name', 'representative_phone', 'address', 'is_deleted')
    search_fields = ('company_name', 'representative_name', 'address')
    list_editable = ('is_deleted',)
    ordering = ('company_name',)