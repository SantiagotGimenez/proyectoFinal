# Generated by Django 4.0.3 on 2022-05-10 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_remove_autor_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='fecha_creacion',
        ),
    ]
