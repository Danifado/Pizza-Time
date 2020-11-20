from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id_ciudad = models.SmallintField(primary_key = True)
    nombre = models.CharField(max_length=25)
    id_pais = models.SmallintField(foreign_key = True)
    