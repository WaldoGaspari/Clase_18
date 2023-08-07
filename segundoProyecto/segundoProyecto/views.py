from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

def saludo(request):
    return HttpResponse("Hola bienvenido/a al primer proyecto con Django!")

def saludo_httml(request):
    response = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Estamos usando HTML!!</h2>
    </html>
    """
    return HttpResponse(response)

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es: {dia}"
    return HttpResponse(texto)

def saludo_nombre(request, nombre):
    response = f"""
    <html>
    <h1>Tu nombre es: </h1>
    <h1>{nombre}</h1>
    </html>
    """
    return HttpResponse(response)

def uso_template(request, nombre, apellido):
    notas = [4,8,1,2,9]
    diccionario = {"nombre":nombre, "apellido":apellido, "notas": notas}
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)