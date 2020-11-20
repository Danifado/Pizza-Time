from django.db import models

# Create your models here.
class Direccion (models.Model):
    id_direccion = models.SerialField(primary_key = True)
    descripcion = models.CharField(max_length=100)
    id_cliente = models.SerialField(foreign_key = True)
    id_ciudad = models.SerialField(foreign_key = True)