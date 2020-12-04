from django import forms
from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre',
            'descripcion',
            'precio',
        ]

        fields = {
            'id_producto': 'Id',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
        }

        widgets = {
           'id_producto': forms.TextInput(attrs = {'class': 'form-control' }),
           'nombre': forms.TextInput(attrs = {'class': 'form-control' }),
           'descripcion': forms.TextInput(attrs = {'class': 'form-control' }),
            'precio': forms.TextInput(attrs = {'class': 'form-control' }),    
        }