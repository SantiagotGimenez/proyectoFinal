from django.contrib import admin

# Register your models here.
from .models import Curso, Profesor, Estudiantes, Entregable

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiantes)
admin.site.register(Entregable)