# Generated by Django 4.0.3 on 2022-05-10 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_remove_categoria_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
    ]
