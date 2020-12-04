from django import forms
from apps.cliente.models import Cliente, Carrito, Telefono, Pais, Ciudad, Direccion

# Cliente Form
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields ='__all__'
        
        labels = {
            'id_cliente': 'Id',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'usuario': 'Usuario',
            'correo': 'Correo'
        }

class TelefonoForm(forms.ModelForm):    
    class Meta:
        id_cliente = forms.ModelChoiceField(queryset=Cliente.objects.values('id_cliente'), empty_label=None, to_field_name=None)
        model = Telefono

        fields = ('numero', 'indicativo_pais', 'id_cliente')

        labels = {
            'numero': 'Número de teléfono celular',
            'indicativo_pais': 'Indicativo',
            'id_cliente': 'Tu nombre'
        }


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'

        labels = {
            'id_cliente': 'Nombre',
            'id_ciudad': 'Ciudad'
        }

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = '__all__'