# Generated by Django 4.0.3 on 2022-05-10 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_autor_estado_autor_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='estado',
        ),
    ]
