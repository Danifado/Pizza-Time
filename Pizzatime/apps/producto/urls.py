from django.urls import path
from apps.producto.views import index, crearProducto, consultarProducto, editarProducto, crearAdmin

urlpatterns = [
 path('', index),
 path('crearProducto/', crearProducto),
 path('consultarProducto/', consultarProducto),
 path('editarProducto/<id_prod>', editarProducto, name = 'editarProducto'),
 path('crearAdmin/', crearAdmin)
]
