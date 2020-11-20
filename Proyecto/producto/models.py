from django.db import models

# Create your models here.
class Producto (models.Model):
    id_producto = models.SerialField(primary_key = True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=45)
    precio = models.IntegerField
    id_administrador =  models.SerialField(foreign_key = True)