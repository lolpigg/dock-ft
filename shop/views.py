from django.shortcuts import render, get_object_or_404, redirect

from .forms import SupplierForm
from .models import Product, Supplier


def product_catalog(request):
    products = Product.objects.all()
    return render(request, 'product_catalog.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    tags = product.description.all()
    return render(request, 'product_detail.html', {'product': product, 'tags' : tags})

def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})

def supplier_detail(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    return render(request, 'supplier_detail.html', {'supplier': supplier})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    else:
        form = SupplierForm()
    return render(request, 'add_supplier.html', {'form': form})

