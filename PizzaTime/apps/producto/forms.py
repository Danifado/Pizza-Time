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

        labels = {
            'id_producto': 'Id',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
        }

        widgets = {
           'id_producto': forms.TextInput(),
           'nombre': forms.TextInput(),
           'descripcion': forms.TextInput(),
            'precio': forms.TextInput(),    
        }