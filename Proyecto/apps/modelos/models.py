from django.db import models
from django.contrib import admin

# Create your models here.

#Administrador

class Administrador(models.Model):
    id_administrador = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)

# Carrito 

class Carrito(models.Model):
    id_carrito = models.IntegerField(primary_key = True)
   
#Ciudad

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=25)

#Cliente

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)
    correo = models.CharField(max_length=45)

#Direccion

class Direccion (models.Model):
    id_direccion = models.IntegerField(primary_key = True)
    descripcion = models.CharField(max_length=100)

#Domiciliario 

class Domiciliario (models.Model):
    id_domiciliario = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

#País

class Pais (models.Model):
    id_pais = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=25)

#Pedido

class Pedido (models.Model):
    id_pedido = models.IntegerField(primary_key = True)
    fecha = models.DateField()
    hora = models.TimeField()
    valor_total = models.IntegerField()

#Producto

class Producto (models.Model):
    id_producto = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=45)
    precio = models.IntegerField()

#Sede

class Sede (models.Model):
    id_sede = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)

#Telefono

class Telefono (models.Model):
    numero = models.IntegerField(primary_key = True)
    indicativo_pais = models.IntegerField()

############################################################

admin.site.register(Administrador)
admin.site.register(Carrito)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Domiciliario)
admin.site.register(Pais)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Sede)
admin.site.register(Telefono)
