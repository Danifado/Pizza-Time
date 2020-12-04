from django.urls import path
from apps.cliente.views import index, crearCliente, crearTelefono, crearDireccion, crearPais, crearCiudad

urlpatterns = [
    path('', index),
    path('crearCliente/', crearCliente),
    path('crearTelefono/', crearTelefono),
    path('crearPais/', crearPais),
    path('crearCiudad/', crearCiudad),
    path('crearDireccion/', crearDireccion),
]