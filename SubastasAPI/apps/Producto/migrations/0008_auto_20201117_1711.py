# Generated by Django 3.1.3 on 2020-11-17 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Producto', '0007_auto_20201117_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
