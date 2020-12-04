from django.urls import path
from apps.cliente.views import index, crearCliente, crearTelefono, crearDireccion, crearPais, crearCiudad, crearCarrito, consultarDomiciliario

urlpatterns = [
    path('', index),
    path('crearCliente/', crearCliente),
    path('crearTelefono/', crearTelefono),
    path('crearPais/', crearPais),
    path('crearCiudad/', crearCiudad),
    path('crearDireccion/', crearDireccion),
    path('crearCarrito/', crearCarrito),
    path('consultarDomiciliario/', consultarDomiciliario)
]