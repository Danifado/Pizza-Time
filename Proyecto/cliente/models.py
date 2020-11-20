from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.SerialField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length = 15)
    correo = models.CharField(max_length=45)
    