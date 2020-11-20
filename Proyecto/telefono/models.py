from django.db import models

# Create your models here.
class Telefono (models.Model):
    numero = models.CharField(max_length=10)(primary_key = True)
    indicatvo_pais = models.SmallintField
    id_cliente = models.IntegerField(foreign_key = True)