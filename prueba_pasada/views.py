from django.http import HttpResponse

def simple (request):
    return HttpResponse("<h1>Funcion sin parametros</h1>")

def param (request, nombre):
    result=f"<h1>Bienvenido {nombre}</h1>"
    return HttpResponse(result)

def doble (request, genero, edad):
    result=f"<h1>Usted es {genero} de {edad} años"
    return HttpResponse(result)