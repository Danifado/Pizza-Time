from django import forms
from apps.producto.models import Producto, Administrador

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        labels = {
            'id_producto': 'Id',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
        }

class AdminForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'usuario': 'Usuario'
        }