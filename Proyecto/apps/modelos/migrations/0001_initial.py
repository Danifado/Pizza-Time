# Generated by Django 3.1.3 on 2020-11-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=15)),
            ],
        ),

        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),

        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),

        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=45)),
            ],
        ),

        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),

        migrations.CreateModel(
            name='Domiciliario',
            fields=[
                ('id_domiciliario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),

        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('valor_total', models.IntegerField()),
            ],
        ),
         migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=45)),
                ('precio', models.IntegerField()),
            ],
        ),

        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),

        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('indicatvo_pais', models.IntegerField()),
            ],
        ),

    ]