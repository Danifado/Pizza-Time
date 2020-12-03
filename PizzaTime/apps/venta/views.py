from django.shortcuts import render
from apps.cliente.models import Cliente, Direccion
from .forms import DomiciliarioForm
# Create your views here.

def crearDomiciliario(request):
    form = DomiciliarioForm
    context = {'form', form}
    return render(request, 'venta/crearDomiciliario.html', context)