from django.db import models

# Create your models here.

## Tabla adminsitrador
class Administrador(models.Models):
    id_administracion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)

## Tabla carrito
class Carrito(models.Models):
    id_carrito = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

## Tabla producto
class Producto(models.Models):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=45)
    precio = models.IntegerField()
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_precio = models.ForeingKey(Administrador, on_delete=models.CASCADE)

## Tabla cliente
class Cliente(models.Models):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    usuario = models.CharField(max_length = 15)
    contraseña = models.CharField(max_length = 45)
    correo = models.EmailField(max_length= 100)
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

## Tabla telefono
class Telefono(models.Models):
    numero = models.CharField(max_length=10)
    indicativo_pais = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

## Tabla domiciliario
class Domiciliario(models.Models):
    id_domiciliario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)