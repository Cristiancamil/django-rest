from django.shortcuts import render
from inmuebleslist_app.models import Inmueble
from django.http import JsonResponse


# Create your views here.

def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    data = {
        'inmuebles': list(inmuebles.values())
    }

    return JsonResponse(data)

def inmueble_detalle(request, id):
    inmueble = Inmueble.objects.get(id=id)
    data = {
        'direccion': inmueble.direccion,
        'pais': inmueble.pais,
        'imagen': inmueble.imagen,
        'active': inmueble.active,
        'descripcion': inmueble.descripcion
    }

    return JsonResponse(data)
