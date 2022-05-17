from email.mime import image

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from ecommerce.apps.catalogue.forms import productForm

from .models import Category, Product


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "catalogue/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter( is_active=True,
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "catalogue/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "catalogue/single.html", {"product": product})

def listar_productos(request):
    producto = Product.objects.filter(vendedor=request.user)
    return render(request, "catalogue/listar-productos.html", {"producto": producto})

def agregar_productos(request):
    data = {
        'form' : productForm()
    }
    
    if request.method == 'POST':
        formulario = productForm(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect(to='http://127.0.0.1:8000/listar-productos/')
        else:
            data['form'] = formulario
    return render(request, "catalogue/agregar-productos.html", data)

def editar_producto(request, id):
    producto = get_object_or_404(Product, pk=id)
    data = {
        'form' : productForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = productForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto editado correctamente')
            return redirect(to='http://127.0.0.1:8000/listar-productos/')
        data['form'] = formulario
    return render(request, "catalogue/editar-producto.html", data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Product, pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect(to='http://127.0.0.1:8000/listar-productos/')
