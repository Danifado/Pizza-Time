from django.urls import path
# IMPORTAR LAS VIEWS
from apps.venta.views import create_domiciliario


urlpatterns = [
    path('create_domiciliario/', create_domiciliario(), name="create_domiciliario"),
]