from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import cursoFormulario
# Create your views here.
def curso(self):
    
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"----> Curso: {curso.nombre} Camada:{curso.camada}"

    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')

def entregables(request):
    return render(request,'AppCoder/entregables.html')

def padre(request):
    return render(request, 'AppCoder/padre.html')

def formularioCurso(request):
    
    if request.method == 'POST':

        miFormulario = cursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = cursoFormulario()
    
    return render(request, 'AppCoder/FormularioCurso.html', {"miFormulario":miFormulario})

def busquedaCamada(request):
    
    return render(request, "AppCoder/BusquedaCamada.html")

def buscar(request):

    respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"

    return HttpResponse(respuesta)