from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)