from django.db import models
from django.contrib import admin

## Tabla adminsitrador


class Administrador(models.Model):
    id_administrador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)

## Tabla producto


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=45)
    precio = models.IntegerField()
    id_administrador = models.ForeignKey(
        Administrador, on_delete=models.CASCADE)

## Tabla carrito


class Carrito(models.Model):
    id_carrito = models.IntegerField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

## Tabla cliente


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=45)
    correo = models.EmailField(max_length=100)
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

## Tabla telefono


class Telefono(models.Model):
    numero = models.CharField(max_length=10)
    indicativo_pais = models.IntegerField(default=1)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

## Tabla domiciliario


class Domiciliario(models.Model):
    id_domiciliario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

#Tabla Pais


class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=20)

#Tabla Ciudad


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=20)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

#Tabla Direccion


class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    calle = models.IntegerField()
    numero_1 = models.IntegerField()
    numero_2 = models.IntegerField()
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

#Tabla Sede


class Sede(models.Model):
    id_sede = models.IntegerField(primary_key=True)
    nombre_sede = models.CharField(max_length=20)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

#Tabla Pedido


class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    valor_total = models.IntegerField()
    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    id_domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)


admin.site.register(Administrador)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Telefono)
admin.site.register(Domiciliario)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Direccion)
admin.site.register(Sede)
admin.site.register(Pedido)
