from django.db import models

# Create your models here.
class Sede (models.Model):
    id_sede = models.SerialField(primary_key = True)
    nombre = models.CharField(max_length=20)
    id_direccion = models.SerialField(foreign_key = True)