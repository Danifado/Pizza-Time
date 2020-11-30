from django.db import models
from django.contrib import admin

# Create your models here.

#Administrador

class Administrador(models.Model):
    id_administrador = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)

#Producto

class Producto (models.Model):
    id_producto = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    id_administrador = models.ForeignKey(Administrador, on_delete= models.CASCADE)

admin.site.register(Producto)
admin.site.register(Administrador)
