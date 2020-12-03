from django.db import models
from django.contrib import admin
from apps.producto.models import Producto

# Create your models here.

#Cliente

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)
    correo = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre + " " +self.apellido

# Carrito

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key = True)
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete= models.CASCADE)

#Telefono

class Telefono (models.Model):
    numero = models.BigIntegerField(primary_key = True)
    indicativo_pais = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)

# País

class Pais (models.Model):
    id_pais = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

#Ciudad

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=25)
    id_pais = models.ForeignKey(Pais, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre

#Direccion

class Direccion (models.Model):
    id_direccion = models.IntegerField(primary_key = True)
    descripcion = models.CharField(max_length=100)
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, on_delete= models.CASCADE)


admin.site.register(Carrito)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Telefono)
admin.site.register(Pais)


