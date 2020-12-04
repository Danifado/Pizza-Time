from django.shortcuts import render, redirect
#from django.httm import HttpResponse
from apps.producto.models import Producto
from apps.producto.forms import ProductoForm, AdminForm

# Create your views here.

def index(request):
    return render(request, 'producto/inicio.html')

def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        form.save()
    else:
        form = ProductoForm()
    return render(request, 'producto/crearProducto.html', {'form': form})

def consultarProducto(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'producto/consultarProducto.html', contexto)

def editarProducto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return ConsultarProducto(request)
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'producto/editarProducto.html', {'form': form})

def crearAdmin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/producto/consultarProducto')
    else:
        form = AdminForm()
    context ={'form':form}
    return render(request, 'producto/crearAdmin.html', context)