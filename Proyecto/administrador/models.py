from django.db import models

# Create your models here.
class Administrador(models.Model):
    id_administrador = models.SerialField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)
