from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.cliente.models import Cliente
from apps.cliente.forms import ClienteForm, TelefonoForm, PaisForm, CiudadForm, DireccionForm, CarritoForm

# Create your views here.

def index(request):
    return render(request, 'cliente/inicio.html')

def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cliente/crearTelefono')
    else:
        form = ClienteForm()
    return render(request, 'cliente/crearCliente.html', {'form': form})

def crearTelefono(request):
    form = TelefonoForm()
    Clientes = Cliente.objects.all()
    if request.method == 'POST':
        form = TelefonoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cliente/crearDireccion')

    context = {'form': form, 'Clientes':Clientes}
    return render(request, 'cliente/crearTelefono.html', context)

def crearPais(request):
    pform = PaisForm()
    if request.method == 'POST':
        pform = PaisForm(request.POST)
        # cform = CiudadForm(request.POST)
        # dform = DireccionForm(request.POST)
        # if (pform.is_valid() & cform.is_valid() & dform.is_valid()):
        if (pform.is_valid()):
            pform.save()
            return redirect('/cliente/crearCiudad')
    
    # context = {'pform': pform, 'cform': cform, 'dform': dform}
    context = {'pform': pform}
    return render(request, 'cliente/crearPais.html', context)

def crearCiudad(request):
    cform = CiudadForm()
    if request.method == 'POST':
        cform = CiudadForm(request.POST)
        if (cform.is_valid()):
            cform.save()
            return redirect('/cliente/crearDireccion')
    context = {'cform': cform}
    return render(request, 'cliente/crearCiudad.html', context)

def crearDireccion(request):
    dform = DireccionForm()
    if request.method == 'POST':
        dform = DireccionForm(request.POST)
        if (dform.is_valid()):
            dform.save()
            return redirect('/cliente/crearPais')
    context = {'dform': dform}
    return render(request, 'cliente/crearDireccion.html', context)
    # dform = DireccionForm()

def crearCarrito(request):
    if request.method == 'POST':
        form = CarritoForm(request.POST)
        if (form.is_valid()):
            form.save()
    else:
        form = CarritoForm()
    context = {'form': form}
    return render(request, 'venta/crearCarrito.html', context)