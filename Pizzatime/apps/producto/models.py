from django.db import models
from django.contrib import admin

# Create your models here.

#Administrador

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)

    def __str__(self):
        return str(self.id_administrador) + ' - ' + self.nombre + ' '+ self.apellido

#Producto

class Producto(models.Model):
    id_producto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    id_administrador = models.ForeignKey(Administrador, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.id_producto) + ' - ' + self.nombre + ': ' +str(self.precio)

admin.site.register(Producto)
admin.site.register(Administrador)
