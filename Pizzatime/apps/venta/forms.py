from django import forms
from .models import Domiciliario, Sede, Pedido

# Cliente Forms
class DomiciliarioForm(forms.ModelForm):
    class Meta:
        model = Domiciliario

        fields = '__all__'
        
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido'
        }

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede 

        fields = '__all__'

        labels = {
            'nombre': 'Nombre de la Sede',
            'direccion': 'Dirección'
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido

        fields = '__all__'

        labels = {
            'fecha': 'Fecha de entrega',
            'hora': 'Hora de entrega',
            'valor_total': 'Valor del pedido',
            'id_cliente': 'Cliente',
            'id_direccion': 'Dirección de envío',
            'id_sede': 'Sede más cercana',
            'id_domiciliario': 'Domiciliario'
        }
