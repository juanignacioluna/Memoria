from django.http import *
from polls.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):

    return HttpResponse("Index")


@csrf_exempt
def final(request):


    data = json.loads(request.body.decode('utf-8'))

    listaResultados = serializers.serialize("json", tablaDeResultados.objects.all())

    conclusion = "no existe"

    for x in json.loads(listaResultados):

        if (x["fields"]["nombre"]==data['nombre']):
            conclusion = "existe"


    if (conclusion=="existe"):

        resultado = tablaDeResultados.objects.get(nombre=data['nombre'])

        resultado.ultimoPuntaje=data['puntaje']

        if (resultado.mejorPuntaje < data['puntaje']):

            resultado.mejorPuntaje=data['puntaje']

        resultado.save()

    else:

        resultado = tablaDeResultados(nombre=data['nombre'], ultimoPuntaje=data['puntaje'], mejorPuntaje=data['puntaje'])

        resultado.save()




    return HttpResponse("listo")



@csrf_exempt
def getTabla(request):

    listaResultados = serializers.serialize("json", tablaDeResultados.objects.all().order_by('-mejorPuntaje'))

    data = {"Resultados": json.loads(listaResultados)}

    return JsonResponse(data)
