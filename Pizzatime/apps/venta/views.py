from django.shortcuts import render
from .models import Cliente, Direccion
from .forms import DomiciliarioForm, SedeForm, PedidoForm
# Create your views here.

def crearDomiciliario(request):
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST)
        form.save()
    else:
        form = DomiciliarioForm()
    context = {'form': form}
    return render(request, 'venta/crearDomiciliario.html', context)

def crearSede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        form.save()
    else:
        form = SedeForm()
    context = {'form': form}
    return render(request, 'venta/crearSede.html', context)

def crearPedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        form.save()
    else:
        form = PedidoForm()
    context = {'form': form}
    return render(request, 'venta/crearPedido.html', context)