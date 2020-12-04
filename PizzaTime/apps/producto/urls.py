from django.urls import path
from apps.producto.views import index, CrearProducto, ConsultarProducto, EditarProducto, inicio

urlpatterns = [
 path('', index),
 path('CrearProducto/', CrearProducto),
 path('ConsultarProducto/', ConsultarProducto),
 path('EditarProducto/<id_prod>', EditarProducto, name = 'EditarProducto'),
 path('Inicio/', inicio)
]