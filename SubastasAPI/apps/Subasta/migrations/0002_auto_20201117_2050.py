# Generated by Django 3.1.3 on 2020-11-18 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0009_auto_20201117_1736'),
        ('Subasta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subasta',
            name='Nombre_Producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.producto', unique=True),
        ),
    ]
