from django.db import models

# Create your models here.
class Pais (models.Model):
    id_pais = models.SerialField(primary_key = True)
    nombre = models.CharField(max_length=25)