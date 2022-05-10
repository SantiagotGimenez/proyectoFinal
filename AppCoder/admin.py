from django.contrib import admin

# Register your models here.
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres','apellidos','email']
    list_display = ('nombres','apellidos')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)

