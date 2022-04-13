from django.urls import path
from AppCoder import views




urlpatterns = [
    path('cursos/',views.curso, name="Curso"),
    path('estudiantes/',views.estudiantes),
    path('profesores/',views.profesores),
    path('entregables/',views.entregables, name='Entregables'),
    path('',views.padre),
    path('formulariocurso/', views.formularioCurso, name='FormularioCurso'),
    path('busquedaCamada/', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    
   
    ]
