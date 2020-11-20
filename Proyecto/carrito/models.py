from django.db import models

# Create your models here.

class Carrito(models.Model):
    id_carrito = models.SerialField(primary_key = True)
    id_producto = models.SerialField(foreign_key = True)
    id_cliente = models.SerialField(foreign_key = True)