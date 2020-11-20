from django.db import models

# Create your models here.
class Pedido (models.Model):
    id_pedido = models.SerialField(primary_key = True)
    fecha = models.DateField
    hora = models.TimeField
    valor_total = models.SmallintField
    id_cliente = models.SerialField(foreign_key = True)
    id_sede = models.SerialField(foreign_key = True)
    id_domiciliario = models.SerialField(foreign_key = True)