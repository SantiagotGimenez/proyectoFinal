from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segundaVista(request):
    return HttpResponse('<br><br> Ya entendimos esto, es muy simple :3')

def diaDeHoy(request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    
    return HttpResponse(documentoDeTexto)


def anioNacimiento(self, edad:int) -> int:

    anio_nacimiento = int(datetime.datetime.now().year) - int(edad)
    documentoDeTexto = f"Naci en el anio: {anio_nacimiento}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nom = "Santiago"
    ap = "Gimenez"
    fecha = datetime.datetime.now()
    lista_de_notas = [1,2,3,4,5,6,7,8]
    diccionario ={"nombre":nom, "apellido":ap, "fecha":fecha, "notas" : lista_de_notas}

    plantilla = loader.get_template('template1.html')

    #mi_html = open("/Users/santiagogimenez/Documents/coderhouse/ProyectoFinal/ProyectoFinal/plantilla/template1.html")
    #plantilla = Template(mi_html.read())
    #mi_html.close()
    #mi_contexto = Context(diccionario) #aca tengo que pasar el contexto. En nuestro caso seria el diccionario que creamos arriba con las variables
    #documento = plantilla.render(mi_contexto)

    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

