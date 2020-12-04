from django.urls import path
# IMPORTAR LAS VIEWS
from .views import crearDomiciliario, crearSede, crearPedido


urlpatterns = [
    path('crearDomiciliario/', crearDomiciliario, name="crearDomiciliario"),
    path('crearSede/', crearSede),
    path('crearPedido/', crearPedido)
]