from django.forms import ModelForm
from apps.venta.models import Domiciliario



# Cliente Forms
class DomiciliarioForm(ModelForm):
    class Meta:
        model = Domiciliario

        fields = '__all__'

        # fields = [
        #     'id_cliente',
        #     'nombre',
        #     'apellido',
        #     'usuario',
        #     'correo'
        # ]
        
        labels = {
            'id_domiciliario': 'Id',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
        }

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
           'id_producto': forms.TextInput(),
           'nombre': forms.TextInput(),
           'descripcion': forms.TextInput(),
            'precio': forms.TextInput(),    
        }

