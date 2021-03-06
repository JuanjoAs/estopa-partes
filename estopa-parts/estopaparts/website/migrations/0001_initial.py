# Generated by Django 4.0 on 2022-01-08 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCompra', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
                ('oferta', models.FloatField()),
                ('marca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nif', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('clave', models.CharField(max_length=255)),
                ('tipo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('valoracion', models.ImageField(upload_to='')),
                ('idComprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.usuario')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.producto')),
            ],
        ),
        migrations.CreateModel(
            name='ProductosPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.pedido')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.usuario'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='idComprador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.usuario'),
        ),
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.usuario')),
            ],
        ),
    ]
