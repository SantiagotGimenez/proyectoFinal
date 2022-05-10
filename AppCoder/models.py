import email
from enum import Flag
from pyexpat import model
from select import select
from statistics import mode
from tabnanny import verbose
from django.db import models
from slugify import slugify

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoría Activada/Categoría no Activada',default=True)

class Meta:
    verbose_name= 'Categoría'
    verbose_name_plural= 'Categorías'

def __str__(self):
    return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField('Nombre de Autor', max_length=255, null=False,blank=False)
    apellidos = models.CharField('Apellido de Autor', max_length=255,null=False,blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True,blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)


class Meta:
    verbose_name = 'Autor'
    verbose_name_plural = 'Autores'

def __str__(self):
    return "{0},{1}".format({self.apellidos}, {self.nombres})

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=90,null=False,blank=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length=110, blank= False, null= False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default= True)
    contenido = models.TextField('Contenido', default=None)

class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

def __init__(self):
    return self.titulo