from django.db import models
from django.contrib import admin
from apps.cliente.models import Cliente, Direccion

# Create your models here.

#Domiciliario 

class Domiciliario (models.Model):
    id_domiciliario = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)


#Sede

class Sede (models.Model):
    id_sede = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20)
    id_direccion = models.ForeignKey(Direccion, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre

#Pedido

class Pedido (models.Model):
    id_pedido = models.AutoField(primary_key = True)
    fecha = models.DateField()
    hora = models.TimeField()
    valor_total = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    id_sede = models.ForeignKey(Sede, on_delete= models.CASCADE)
    id_domiciliario = models.ForeignKey(Domiciliario, on_delete= models.CASCADE)

admin.site.register(Domiciliario)
admin.site.register(Sede)
admin.site.register(Pedido)