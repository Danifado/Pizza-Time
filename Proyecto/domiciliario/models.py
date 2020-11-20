from django.db import models

# Create your models here.
class Domiciliario (models.Model):
    id_domiciliario = models.SerialField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    