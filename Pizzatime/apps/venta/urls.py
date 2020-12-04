from django.urls import path
# IMPORTAR LAS VIEWS
from .views import crearDomiciliario, crearSede, crearPedido, consultarDomiciliario


urlpatterns = [
    path('crearDomiciliario/', crearDomiciliario, name="crearDomiciliario"),
    path('crearSede/', crearSede),
    path('crearPedido/', crearPedido),
    path('consultarDomiciliario/', consultarDomiciliario),
]
