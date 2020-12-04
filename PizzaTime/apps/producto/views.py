from django.shortcuts import render
#from django.httm import HttpResponse
from apps.producto.models import Producto
from apps.producto.forms import ProductoForm

# Create your views here.

def index(request):
    return render(request, 'producto/inicio.html')

def inicio(request):
    return render(request, 'inicio.html')

def CrearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        form.save()
    else:
        form = ProductoForm()
    return render(request, 'producto/CrearProducto.html', {'form': form})

def ConsultarProducto(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'producto/ConsultarProducto.html', contexto)

def EditarProducto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return ConsultarProducto(request)
        else:
            form = ProductoForm(instance=producto)
            return render(request, 'producto/EditarProducto.html', {'form': form})